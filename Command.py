from google.oauth2.credentials import Credentials

class Command():
    def __init__(self, help_str: str) -> None:
        self.help = help_str

    def execute(self, *args: Any) -> None:
        pass
