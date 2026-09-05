import base64
import email
from email import policy
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from config import API_NAME, API_VERSION

class Command():
    def __init__(self, help_str: str) -> None:
        self.help = help_str


    def build_service(self, state: StateClient, *args: type[Any]) -> Resource:
        try:
            service = build(API_NAME, API_VERSION, credentials=state.creds)
        except:
            raise Exception("Cannot build Gmail service")
        return service


    def execute(self, *args: type[Any]) -> None:
        pass


    def get_messages(self, state: StateClient, service: Resource, results: Resource) -> None:
        state.message_ids = []
        index = 0
        for message in results["messages"]:
            state.message_ids.append(message["id"])
            msg_detail = service.users().messages().get(userId="me", id=message["id"], format="raw").execute()
            msg_bytes = base64.urlsafe_b64decode(msg_detail["raw"].encode("ASCII"))
            mime_msg = email.message_from_bytes(msg_bytes, policy=policy.default)
            msg_from = mime_msg["from"]
            msg_subject = mime_msg["subject"]
            msg_date = mime_msg["date"]

            index += 1
            if "UNREAD" in msg_detail["labelIds"]:
                green_color = "\033[32m"
                reset_color = "\033[0m"
                print(f"{green_color}Message {index:2}: Date {msg_date[:26]} From {msg_from}")
                print(f"            Subject: {msg_subject[:150]}{reset_color}")
            else:
                print(f"Message {index:2}: Date {msg_date[:26]} From {msg_from}")
                print(f"            Subject: {msg_subject[:150]}")


