from ListCommand import ListCommand
from config import MAX_RES

class CurrentPageCommand(ListCommand):
    def __init__(self):
        help_str = "List emails in the current page"
        super().__init__(help_str)


    def execute(self, state: StateClient, *args: type[Any]) -> None:
        label_id = state.labels[state.curr_label]["id"]
        service = self.build_service(state)
        results = None

        if not state.next_tokens:
            return None

        # read the messages from account
        if state.next_tokens and len(state.next_tokens) > 1:
            next_token_idx = len(state.next_tokens) - 2
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

        # list the messages 
        self.get_messages(state, service, results)
        service.close()
