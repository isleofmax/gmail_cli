import os
import sys
import json
from email.utils import parseaddr
from Command import Command
from ListLabelsCommand import ListLabelsCommand
from command_list import prompt_cmd
from config import CONFIG_FILE, SCOPES, OS_RELEASE
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from StateClient import StateClient

def is_valid_gmail_address(email: str) -> bool:
    parsed_addr = parseaddr(email)
    if not parsed_addr[1]:
        return False
    if not email.find("@"):
        return False
    if not email.endswith("@gmail.com"):
        return False
    return True


def get_is_wsl() -> bool:
    if not os.path.exists(OS_RELEASE):
        return False

    os_release = ""
    with open(OS_RELEASE, "r") as file:
        os_release = file.read()
    if os_release.lower().find("microsoft") and os_release.lower().find("WSL"):
        return True
    return False


def get_credentials(email_addr: str, path: str, secret_file: str, scopes: list[str]) -> Credentials | None:
    creds = None
    try:
        flow = InstalledAppFlow.from_client_secrets_file(secret_file, SCOPES)

        is_wsl = get_is_wsl()
        if is_wsl:
            creds = flow.run_local_server(
                port=0, 
                open_browser=False, 
                access_type="offline",
                login_hint=email_addr
            )
        else:
            creds = flow.run_local_server(
                port=0,
                open_browser=False, 
                access_type="offline",
                login_hint=email_addr
            )
    except Exception as e:
        print(f"Error: {e}")
    return creds


def connect_to_gmail(email_addr: str, secret_file: str) -> Credentials | None:
    # controls if there is the credentials token file
    creds = None
    token_path = ".".join([email_addr, "json"]).replace("@", "_")
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    
    # if there isn't or its not valid it try to refresh the token
    # or do the oauth2 request for another token
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            creds = get_credentials(email_addr, secret_file, SCOPES)
            if not creds:
                return
        
        # write the token to file with the name of the account selected
        with open(token_path, "w") as file:
            file.write(creds.to_json())
    return creds


def extract_args(line: str) -> list[str]:
    args = line.split()
    return args


def prompt(state: StateClient) -> None:
    print('type "help" for help')
    while True:
        line = input("gmail_cli> ")
        if not line:
            continue

        args = extract_args(line)
        command = args[0]
        if not command in prompt_cmd:
            print("command not found")
            continue

        if command == "help":
            prompt_cmd[command].execute(state, prompt_cmd)
        elif command == "exit" or command == "quit":
            prompt_cmd[command].execute(state)
        else:
            prompt_cmd[command].execute(state, *args[1:])
        print('type "help" for help')



def main() -> None:
    # you must give your gmail address
    command = sys.argv[0]
    if len(sys.argv) != 2:
        print(f"Usage {command} <e-mail address>")
        return

    # controls if you give a valid gmail address
    # (it only controls if is an e-mail address and if there is @gmail.com)
    email_addr = sys.argv[1]
    if not is_valid_gmail_address(email_addr.lower()):
        print(f"You must provide a valid gmail address")
        return

    # controls if the configuration file (the one with secrets keys)
    # is present or not
    if not os.path.exists(CONFIG_FILE):
        print(f"Cannot find config file {CONFIG_FILE}")
        return

    # read the config file to find the file with google credentials
    config_path = ""
    with open(CONFIG_FILE, "r") as file:
        config = file.read()
        config_dict = json.loads(config)
        if "secret" in config_dict:
            config_path = config_dict["secret"]
        else:
            print("Config file doesn't have secret key")
            return

    # try to connect to gmail with the secret key
    creds = connect_to_gmail(email_addr, config_path)
    if not creds:
        return

    # create the StateClient static class with some fields:
    # credentials and the current labels to read messages
    state = StateClient()
    state.creds = creds

    # get the labels of your account and get the indice of
    # the INBOX label from the labels list. If there's an
    # error go out
    try:
        list_labels = ListLabelsCommand()
    except Exception as e:
        print(f"Error: {e}")
        return

    try:
        state.labels = list_labels.get_labels(state)
    except Exception as e:
        print(f"Error: {e}")
        return

    # if you have no labels go out
    if not state.labels:
        print("Cannot get labels from your Gmail account")
        return

    for i in range(len(state.labels)):
        if state.labels[i]["id"] == "INBOX":
            state.curr_label = i
            break

    # do the command prompt
    prompt(state)


if __name__ == "__main__":
    main()
