from Command import Command

class NextCommand(Command):
    def __init__(self):
        help_str = "List emails in your current label (INBOX)"
        super().__init__(help_str)


    def execute(self, cmds: dict[str, Command]) -> None:
        for k in cmds:
            print(f"{k:7}: {cmds[k].help}")
