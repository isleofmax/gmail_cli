from ListCommand import ListCommand
from config import MAX_RES

class PrevCommand(ListCommand):
    def __init__(self):
        help_str = "List previous page of e-mails in the current label"
        super().__init__(help_str)


    def execute(self, state: StateClient, *args: type[Any]) -> None:
        label_id = state.labels[state.curr_label]["id"]
        service = self.build_service(state)
        results = None

        if not state.next_tokens or len(state.next_tokens) == 1:
            return None

        if len(state.next_tokens) == 2:
            results = service.users().messages().list(
                userId="me",
                maxResults=MAX_RES,
                labelIds=label_id,
            ).execute()
            state.next_tokens = []
        else:
            state.next_tokens = state.next_tokens[:-2]
            prev_token_idx = len(state.next_tokens) - 1
            prev_token = state.next_tokens[prev_token_idx]
            results = service.users().messages().list(
                userId="me",
                maxResults=MAX_RES,
                labelIds=label_id,
                pageToken=prev_token
            ).execute()

        if not results:
            print("Error retrieving messages")

        if "nextPageToken" in results:
            state.next_tokens.append(results["nextPageToken"])

        # list the messages 
        self.get_messages(state, service, results)
        service.close()
