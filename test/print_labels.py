import os
import sys
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def main():
    sys.path.append(".")
    from config import SCOPES, SECRET, API_NAME, API_VERSION

    if len(sys.argv) != 2:
        print("Usage print_labels <email address>")
        return

    email_addr = sys.argv[1]
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
            flow = InstalledAppFlow.from_client_secrets_file(SECRET, SCOPES)
            creds = flow.run_local_server(
                port=0, 
                open_browser=False, 
                access_type="offline",
                login_hint=email_addr
            )
            if not creds:
                return
        
        # write the token to file with the name of the account selected
        with open(token_path, "w") as file:
            file.write(creds.to_json())

    service = build(API_NAME, API_VERSION, credentials=creds)
    results = service.users().messages().list(userId="me").execute()
    print(results["messages"])
    print(results["nextPageToken"])

    results = service.users().messages().list(userId="me",pageToken=results["nextPageToken"]).execute()
    print(results["messages"])
    service.close()


if __name__ == "__main__":
    main()
