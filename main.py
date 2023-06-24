import rich
import rich.console
from modules import print_information
console = rich.console.Console()
version = "v0.1"
# console.print("[blue]       ----------------------------------")
# console.print("[blue]      /  [green]____   [red]_  __ [blue]_____ [purple]____       [blue]/")
# console.print("[blue]     /  [green]/ ___| [red]| |/ /[blue]|  ___[purple]|  _  \\    [blue]/")
# console.print("[blue]    /   [green]\\___ \\ [red]| ' / [blue]| |_  [purple]| |_) |   [blue]/")
# console.print("[blue]   /     [green]___) |[red]| . \\ [blue]|  _| [purple]|  __/   [blue]/")
# console.print("[blue]  /     [green]|____/ [red]|_|\\_\\",end="")
# console.print("[blue]|__|  [purple]|_|     [blue]/")
print_information.printCopyrightInformation(2023,version,console)
