import os
from config import TOKEN_PATH, CONFIG_PATH, SCOPES, OS_RELEASE
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

def get_is_wsl() -> bool:
    if not os.path.exists(OS_RELEASE):
        return False

    os_release = ""
    with open(OS_RELEASE, "r") as file:
        os_release = file.read()
    if os_release.lower().find("microsoft") and os_release.lower().find("WSL"):
        return True
    return False


def get_credentials(path: str, scopes: List[str]) -> Credentials | None:
    creds = None
    try:
        flow = InstalledAppFlow.from_client_secrets_file(CONFIG_PATH, SCOPES)

        is_wsl = get_is_wsl()
        if is_wsl:
            creds = flow.run_local_server(port=0, open_browser=False)
        else:
            creds = flow.run_local_server(port=0)
    except Exception as e:
        print(f"Error: {e}")
    return creds


def main() -> None:
    if not os.path.exists(CONFIG_PATH):
        print(f"Cannot find config file {CONFIG_PATH}")
        return

    # controls if there is the credentials token file
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    
    # if there isn't or its not valid it try to refresh the token
    # or do the oauth2 request for another token
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            creds = get_credentials(CONFIG_PATH, SCOPES)
            if not creds:
                return
        with open(TOKEN_PATH, "w") as file:
            file.write(creds.to_json())

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


if __name__ == "__main__":
    main()
