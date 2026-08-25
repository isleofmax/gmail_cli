from Command import Command
from config import MAX_RES

class PrevCommand(Command):
    def __init__(self):
        help_str = "List emails in your current label"
        super().__init__(help_str)


    def execute(self, state: StateClient, *args: type[Any]) -> None:
        label_id = state.labels[state.curr_label]["id"]
        service = self.build_service(state)
        results = None

        if not state.next_tokens or len(state.next_tokens) == 1:
            return None

        print(state.next_tokens)
        if len(state.next_tokens) == 2:
            results = service.users().messages().list(
                userId="me",
                maxResults=MAX_RES,
                labelIds=label_id,
            ).execute()
            state.next_tokens = []
        else:
            state.next_tokens.pop()
            prev_token = state.next_tokens.pop()
            results = service.users().messages().list(
                userId="me",
                maxResults=MAX_RES,
                labelIds=label_id,
                pageToken=prev_token
            ).execute()

        if not results:
            print("Error retrieving messages")

        # list the messages 
        state.ids = []
        index = 0
        for message in results["messages"]:
            state.ids.append(message["id"])
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

        service.close()
