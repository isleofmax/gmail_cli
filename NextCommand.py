from Command import Command
from config import MAX_RES

class NextCommand(Command):
    def __init__(self):
        help_str = "List emails in your current label"
        super().__init__(help_str)


    def execute(self, state: StateClient, *args: type[Any]) -> None:
        label_id = state.labels[state.curr_label]["id"]
        service = self.build_service(state)
        results = None

        # read the messages from account
        if state.next_tokens:
            next_token_idx = len(state.next_tokens) - 1
            next_token = state.next_tokens[next_token_idx]
            results = service.users().messages().list(
                userId="me",
                maxResults=MAX_RES,
                labelIds=label_id,
                pageToken=next_token
            ).execute()
        else:
            results = service.users().messages().list(
                userId="me",
                maxResults=MAX_RES,
                labelIds=label_id,
            ).execute()

        if not results:
            print("Error retrieving messages")

        if "nextPageToken" in results:
            state.next_tokens.append(results["nextPageToken"])

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
