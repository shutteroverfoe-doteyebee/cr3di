from rich.table import Table
from rich.console import Console
from cr3di.storage import load_credentials

def list_creds():
    creds = load_credentials()
    if not creds:
        print("[!] No credentials stored.")
        return

    table = Table(title="Stored Credentials")
    table.add_column("#", style="cyan", no_wrap=True)
    table.add_column("Username", style="green")
    table.add_column("Description")
    table.add_column("Domain", style="magenta")
    table.add_column("IP", style="yellow")

    for i, c in enumerate(creds, 1):
        table.add_row(str(i), c.username, c.description, c.domain or "-", c.ip or "-")

    Console().print(table)

