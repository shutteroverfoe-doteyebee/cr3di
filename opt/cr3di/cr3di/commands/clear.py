import typer
from cr3di.storage import clear_credentials

def clear():
    clear_credentials()
    typer.echo("[+] All credentials wiped.")
