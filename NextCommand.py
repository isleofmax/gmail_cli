from Command import Command

class NextCommand(Command):
    def __init__(self):
        help_str = "List emails in your current label"
        super().__init__(help_str)


    def execute(self, state: StateClient, *args: type[Any]) -> None:
        label_id = state.labels[state.curr_label]["id"]
        service = self.build_service(state)
        results = None
        if state.next_token:
            results = service.users().messages().list(
                userId="me",
                maxResults=10,
                labelIds=label_id,
                pageToken=state.next_token
            ).execute()
            if not state.curr_token:
                state.curr_token = state.next_token
        else:
            results = service.users().messages().list(
                userId="me",
                maxResults=10,
                labelIds=label_id
            ).execute()
            first_next_token = results["nextPageToken"]

        if not results:
            print("Error retrieving messages")

        state.prev_token = state.next_token
        state.next_token = results["nextPageToken"]
        message = results["messages"][1]
        msg_details = service.users().messages().get(userId="me", id=message["id"], format="full").execute()
        print(msg_details)
        service.close()
