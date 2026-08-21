from Command import Command
from StateClient import StateClient

class ListLabelsCommand(Command):
    def __init__(self):
        help_str = "List labels of your gmail account"
        super().__init__(help_str)


    def get_labels(self, state: StateClient) -> List[dict[str, str]]:
        # return the resource service
        service = self.build_service(state)

        # read all the labels of your account
        results = service.users().labels().list(userId="me").execute()
        gmail_labels = results.get("labels", [])
        service.close()

        labels = []
        if gmail_labels:
            for l in gmail_labels:
                labels.append({"id": l["id"], "name": l["name"]})

        return labels


    def execute(self, state: StateClient) -> None:
        # saves the name of your current label and the index
        curr_label_name = state.labels[state.curr_label]['name']

        try:
            state.labels = self.get_labels(state)
            if not state.labels:
                print("No labels found")
                return
            
            # print all the labels you have in your account and
            # reset the index of your current label because you
            # could add labels via web browser and so the index
            # could be wrong
            for i in range(len(state.labels)):
                if curr_label_name == state.labels[i]["name"]:
                    state.curr_label = i
                    print(f"*{i:2}) {state.labels[i]['name']}")
                else:
                    print(f" {i:2}) {state.labels[i]['name']}")
        except Exception as e:
            print(f"Error: {e}")
            return
