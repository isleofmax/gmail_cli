import base64
import email
from bs4 import BeautifulSoup
from email import policy
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

        #get the id of the message
        message_id = state.message_ids[index]

        #get the message in raw format
        message = service.users().messages().get(userId="me", id=message_id, format="raw").execute()

        #convert raw base64 message in bytes
        msg_bytes = base64.urlsafe_b64decode(message["raw"].encode("ASCII"))

        #convert bytes in mime format
        mime_msg = email.message_from_bytes(msg_bytes, policy=policy.default)

        #convert mime format in html
        html_doc = mime_msg.get_body(preferencelist=("plain", "html")).get_content()

        #use BeautifulSoup library to extract text from html and print it
        soup = BeautifulSoup(html_doc, "html.parser")
        print(soup.get_text(separator="\n", strip=True))

        #if the email was marked UNREAD delete this label from the list
        #to mark message like read
        if "UNREAD" in message["labelIds"]:
            service.users().messages().modify(userId="me", id=message_id, body={"removeLabelIds": ["UNREAD"]}).execute()
        service.close


    def _err_email_message(self) -> None:
        print("e-mail not found")

