from ChangeLabelCommand import ChangeLabelCommand
from CurrentLabelCommand import CurrentLabelCommand
from ExitCommand import ExitCommand
from HelpCommand import HelpCommand
from ListLabelsCommand import ListLabelsCommand
from NextCommand import NextCommand

prompt_cmd = {
    "listl": ListLabelsCommand(),
    "currl": CurrentLabelCommand(),
    "changel": ChangeLabelCommand(),
    "next": NextCommand(),
    "help": HelpCommand(),
    "exit": ExitCommand(),
    "quit": ExitCommand()
}
