from Command import Command

class ClearScreenCommand(Command):
    def __init__(self):
        help_str = "Clear the screen"
        super().__init__(help_str)


    def execute(self, state: StateClient, *args: type[Any]) -> None:
        import os
        import sys
        if sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")

