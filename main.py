import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

TOKEN_PATH = "token.json"
CONFIG_PATH = ".env.json"
SCOPES = ["https://mail.google.com/"] 

def main():
    if not os.path.exists(CONFIG_PATH):
        print(f"Cannot find config file {CONFIG_PATH}")
        return

    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CONFIG_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, "w") as file:
            file.write(creds.to_json())
    try:
        service = build("gmail", "v1", credentials=creds)
        results = service.users().labels().list(userId="me").execute()
        labels = results.get("labels", [])
        if not labels:
            print("No labels found")
        else:
            print("labels:")
            for l in labels:
                print(l["name"])
        service.close()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
