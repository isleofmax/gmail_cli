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
            if not labels:
                print("No messages found")
            else:
                for l in labels:
                    print(l["name"])
            service.close()
        except Exception as e:
            print(f"Error: {e}")
            return
