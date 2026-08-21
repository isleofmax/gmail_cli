from HelpCommand import HelpCommand
from ExitCommand import ExitCommand
from ListLabelsCommand import ListLabelsCommand
from NextCommand import NextCommand

prompt_cmd = {
    "listl": ListLabelsCommand(),
    "next": NextCommand(),
    "help": HelpCommand(),
    "exit": ExitCommand(),
    "quit": ExitCommand()
}
