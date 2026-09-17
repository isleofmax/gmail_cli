import os
import sys
from Command import Command
from StateClient import StateClient
from typing import Any

class ClearScreenCommand(Command):
    def __init__(self):
        help_str = "Clear the screen"
        super().__init__(help_str)


    def execute(self, state: StateClient, *args: Any) -> None:
        if sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")

