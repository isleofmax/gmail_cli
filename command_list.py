from ChangeLabelCommand import ChangeLabelCommand
from ClearScreenCommand import ClearScreenCommand
from CurrentLabelCommand import CurrentLabelCommand
from ExitCommand import ExitCommand
from HelpCommand import HelpCommand
from ListLabelsCommand import ListLabelsCommand
from NextCommand import NextCommand
from PrevCommand import PrevCommand

prompt_cmd = {
    "listl": ListLabelsCommand(),
    "currl": CurrentLabelCommand(),
    "changel": ChangeLabelCommand(),
    "clear": ClearScreenCommand(),
    "next": NextCommand(),
    "prev": PrevCommand(),
    "help": HelpCommand(),
    "exit": ExitCommand(),
    "quit": ExitCommand()
}
