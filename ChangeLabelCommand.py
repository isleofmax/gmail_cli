from Command import Command
from StateClient import StateClient

class ChangeLabelCommand(Command):
    def __init__(self):
        help_str = "Change the label of your gmail account where you are in"
        super().__init__(help_str)


    def execute(self, state: StateClient, *args: type[Any]) -> None:
        if len(args) != 1:
            print("Usage changel <number of the label>")
            return

        index = state.curr_label
        try:
            index = int(args[0])
            if index < 1 or index > len(state.labels):
                print(f"You must provide a number from 1 to {len(state.labels)}")
                return
            state.next_token = []
        except:
            print("You must provide a number")

