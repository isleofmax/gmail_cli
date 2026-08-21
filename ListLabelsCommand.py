from Command import Command
from StateClient import StateClient

class ListLabelsCommand(Command):
    def __init__(self):
        help_str = "List labels of your gmail account"
        super().__init__(help_str)


    def execute(self, state: StateClient) -> None:
        try:
            # return the resource service
            service = super().build_service(state)

            # read all the labels of your account
            results = service.users().labels().list(userId="me").execute()
            labels = results.get("labels", [])
            if not messages:
                print("No messages found")
            else:
                print("messages:")
                for m in messages:
                    print(m["id"])
            service.close()
        except Exception as e:
            print(f"Error: {e}")
            return
