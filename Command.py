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
