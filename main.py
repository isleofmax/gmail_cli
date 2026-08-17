import os
import sys
from email.utils import parseaddr
from Command import Command
from command_list import prompt_cmd
from config import CONFIG_PATH, SCOPES, OS_RELEASE
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

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


def get_credentials(email_addr: str, path: str, scopes: List[str]) -> Credentials | None:
    creds = None
    try:
        flow = InstalledAppFlow.from_client_secrets_file(CONFIG_PATH, SCOPES)

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


def connect_to_gmail(email_addr: str) -> Credentials | None:
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
            creds = get_credentials(email_addr, CONFIG_PATH, SCOPES)
            if not creds:
                return

        with open(token_path, "w") as file:
            file.write(creds.to_json())
    return creds


def find_command(line: str) -> str:
    command = line.split()[0]
    return command


def prompt() -> None:
    while True:
        line = input("gmail_cli> ")
        if not line:
            continue

        command = find_command(line)
        if not command in prompt_cmd:
            print("command not found")
            continue

        if command == "help":
            prompt_cmd[command].execute(prompt_cmd)
        else:
            prompt_cmd[command].execute()


def gmail_functs() -> None:
    try:
        # read the messages you have in gmail
        service = build("gmail", "v1", credentials=creds)
        results = service.users().messages().list(userId="me").execute()
        messages = results.get("messages", [])
        if not messages:
            print("No messages found")
        else:
            print("messages:")
            for m in messages:
                print(m["id"])
        service.close()
    except Exception as e:
        print(f"Error: {e}")
        return


def main() -> None:
    # controls if the configuration file (the one with secrets keys)
    # is present or not
    if not os.path.exists(CONFIG_PATH):
        print(f"Cannot find config file {CONFIG_PATH}")
        return

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

    creds = connect_to_gmail(email_addr)
    if not creds:
        return

    prompt()


if __name__ == "__main__":
    main()
