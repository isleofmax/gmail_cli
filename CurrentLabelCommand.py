from Command import Command
from StateClient import StateClient

class CurrentLabelCommand(Command):
    def __init__(self):
        help_str = "Display the label of your gmail account where you are in"
        super().__init__(help_str)


    def execute(self, state: StateClient, *args: type[Any]) -> None:
        print(f"Current label: {state.labels[state.curr_label]['name']}")
