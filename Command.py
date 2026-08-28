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
            msg_details = service.users().messages().get(userId="me", id=message["id"], format="full").execute()
            msg_from = ""
            msg_subject = ""
            msg_date = ""
            for header in msg_details["payload"]["headers"]:
                if header["name"] == "From":
                    msg_from = header["value"]
                elif header["name"] == "Date":
                    msg_date = header["value"]
                elif header["name"] == "Subject":
                    msg_subject = header["value"]

            index += 1
            print(f"Message {index:2}: Date {msg_date[:26]} From {msg_from}")
            print(f"            Subject: {msg_subject[:150]}")


