from Command import Command

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


    def execute(self, state: StateClient, *args: type[Any]) -> None:
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
            index = 1
            for label in state.labels:
                if curr_label_name == label["name"]:
                    state.curr_label = index - 1
                    print(f"*{index:2}) {label['name']}")
                else:
                    print(f" {index:2}) {label['name']}")
                index += 1
        except Exception as e:
            print(f"Error: {e}")
            return
