class Command():
    def __init__(self, help_str: str) -> None:
        self.help = help_str


    def execute(self) -> None:
        pass


    def execute(self, cmds: Any) -> None:
        pass
