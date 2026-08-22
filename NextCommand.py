from Command import Command

class NextCommand(Command):
    def __init__(self):
        help_str = "List emails in your current label"
        super().__init__(help_str)


    def execute(self, state: StateClient, *args: type[Any]) -> None:
        label_id = labels[state.curr_label]["id"]
        service = self.build_service(state)
        if state.page_token:
            results = service.users().messages().list(
                userId="me",
                labelIds=label_id,
                pageToken=state.page_token
            )
        else:
            results = service.users().messages().list(
                userId="me",
                labelIds=label_id
            )
