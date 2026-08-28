import base64
from bs4 import BeautifulSoup
from Command import Command

class ReadCommand(Command):
    def __init__(self):
        help_str = "Read the selected e-mail"
        super().__init__(help_str)


    def execute(self, state: StateClient, *args: type[Any]) -> None:
        if len(args) != 1:
            print("Usage read <number of the e-mail>")
            return

        index = None
        try:
            index = int(args[0]) - 1
        except:
            self._err_email_message()
            return None

        if index < 0 or index > 19:
            self._err_email_message()
            return None

        service = self.build_service(state)
        message_id = state.message_ids[index]
        msg_details = service.users().messages().get(userId="me", id=message_id, format="full").execute()

        body_data = ""
        for part in msg_details["payload"]["parts"]:
            if "data" in part["body"]:
                body_data += part["body"]["data"]
        if body_data:
            base64_decoded = base64.urlsafe_b64decode(body_data).decode("utf-8", errors="ignore")
            soup = BeautifulSoup(base64_decoded, "html.parser")
            print(soup.get_text(separator="\n", strip=True))
        service.close()


    def _err_email_message(self) -> None:
        print("e-mail not found")

