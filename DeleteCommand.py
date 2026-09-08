import base64
import email
from bs4 import BeautifulSoup
from email import policy
from Command import Command

class DeleteCommand(Command):
    def __init__(self):
        help_str = "Move the selected e-mail to Trash"
        super().__init__(help_str)


    def execute(self, state: StateClient, *args: type[Any]) -> None:
        if state.labels[state.curr_label] == "TRASH":
            print("You cannot delete e-mails from TRASH")
            return

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

        while True:
            resp = input("Are you sure? [y/N]").lower()
            if resp == "y" or resp == "n" or resp == "":
                break
            print(resp)
        if resp != "y":
            return

        #build the service with credentials
        service = self.build_service(state)

        #get the id of the message
        message_id = state.message_ids[index]

        #get the message in raw format
        message = service.users().messages().get(userId="me", id=message_id, format="raw").execute()

        #if the email was marked UNREAD delete this label from the list
        #to mark message like read
        service.users().messages().modify(userId="me", id=message_id, body={"removeLabelIds": message["labelIds"]}).execute()
        if "UNREAD" in message["labelIds"]:
            message["labelIds"] = ["UNREAD", "TRASH"]
        else:
            message["labelIds"] = ["TRASH"]
        service.users().messages().modify(userId="me", id=message_id, body={"addLabelIds": message["labelIds"]}).execute()
        service.close()


    def _err_email_message(self) -> None:
        print("e-mail not found")

