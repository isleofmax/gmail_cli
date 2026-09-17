import sys
from Command import Command
from StateClient import StateClient
from typing import Any

class ExitCommand(Command):
    def __init__(self):
        help_str = "Exit the terminal"
        super().__init__(help_str)


    def execute(self, state: StateClient, *args: Any) -> None:
        print("bye!!\n")
        sys.exit()
