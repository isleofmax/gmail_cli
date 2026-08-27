from Command import Command

class ReadCommand(Command):
    def __init__(self):
        help_str = "Read the selected e-mail"
        super().__init__(help_str)


    def execute(self, state: StateClient, *args: type[Any]) -> None:
        if len(args) != 1:
            print("Usage read <number of the e-mail>")
            return

        service = self.build_service(state)
        service.close()
