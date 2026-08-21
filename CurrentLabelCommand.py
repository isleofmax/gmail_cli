from Command import Command
from StateClient import StateClient

class CurrentLabelCommand(Command):
    def __init__(self):
        help_str = "List labels of your gmail account"
        super().__init__(help_str)


    def execute(self, state: StateClient) -> None:
        print(f"Current label: {state.curr_label}")
