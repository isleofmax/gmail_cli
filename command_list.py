from ChangeLabelCommand import ChangeLabelCommand
from ClearScreenCommand import ClearScreenCommand
from CurrentLabelCommand import CurrentLabelCommand
from CurrentPageCommand import CurrentPageCommand
from ExitCommand import ExitCommand
from HelpCommand import HelpCommand
from ListLabelsCommand import ListLabelsCommand
from NextCommand import NextCommand
from PrevCommand import PrevCommand
from ReadCommand import ReadCommand

prompt_cmd = {
    "listl": ListLabelsCommand(),
    "currl": CurrentLabelCommand(),
    "changel": ChangeLabelCommand(),
    "clear": ClearScreenCommand(),
    "currp": CurrentPageCommand(),
    "next": NextCommand(),
    "prev": PrevCommand(),
    "read": ReadCommand(),
    "help": HelpCommand(),
    "exit": ExitCommand(),
    "quit": ExitCommand()
}
