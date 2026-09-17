from Command import Command
from StateClient import StateClient
from typing import Any

class HelpCommand(Command):
    def __init__(self):
        help_str = "Print help message"
        super().__init__(help_str)


    def execute(self, state: StateClient, *args: Any) -> None:
        cmds: dict[str, Command] = args[0]
        for k in cmds:
            print(f"{k:7}: {cmds[k].help}")
        print()
