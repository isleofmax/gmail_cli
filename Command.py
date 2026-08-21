from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from config import API_NAME, API_VERSION

class Command():
    def __init__(self, help_str: str) -> None:
        self.help = help_str


    def build_service(self, state: StateClient) -> Resource:
        try:
            service = build(API_NAME, API_VERSION, credentials=StateClient.creds)
        except:
            raise Exception
        return service


    def execute(self, *args: Any) -> None:
        pass
