import base64
import email
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
        message_id = state.message_ids[index]
        message = service.users().messages().get(userId="me", id=message_id, format="raw").execute()
        msg_bytes = base64.urlsafe_b64decode(message["raw"].encode("ASCII"))
        mime_msg = email.message_from_bytes(msg_bytes, policy=policy.default)
        print(mime_msg.get_body(preferencelist=("plain", "html")).get_content())a

        # bisogna farlo passare nella libreria beautifulsoup
        # Ora puoi accedere a tutte le parti decodificate in modo semplicissimo:
        #print("Oggetto:", mime_msg['subject'])
        #print("Mittente:", mime_msg['from'])

        service.close()


    def _err_email_message(self) -> None:
        print("e-mail not found")

