import sys
from Command import Command

class ExitCommand(Command):
    def __init__(self):
        help_str = "Exit the terminal"
        super().__init__(help_str)


    def execute(self) -> None:
        print("bye")
        sys.exit()
