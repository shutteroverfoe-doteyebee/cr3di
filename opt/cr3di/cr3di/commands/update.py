import typer
from cr3di.storage import load_credentials, save_credentials
from rich.prompt import Prompt
import subprocess

def update():
    creds = load_credentials()
    if not creds:
        typer.echo("[!] No credentials available.")
        return

    # Use fzf to pick one
    display = [f"{c.username} ({c.description})" for c in creds]
    try:
        fzf = subprocess.run(["fzf"], input="\n".join(display), text=True, capture_output=True)
    except FileNotFoundError:
        typer.echo("[!] fzf is not installed.")
        return

    if not fzf.stdout.strip():
        typer.echo("[*] No selection made.")
        return

    index = display.index(fzf.stdout.strip())
    target = creds[index]

    typer.echo("Leave blank to keep current value.")
    target.username = Prompt.ask("Username", default=target.username)
    target.password = Prompt.ask("Password", default=target.password, password=True)
    target.description = Prompt.ask("Description", default=target.description)
    target.domain = Prompt.ask("Domain", default=target.domain)
    target.ip = Prompt.ask("IP", default=target.ip)

    creds[index] = target
    save_credentials(creds)
    typer.echo("[+] Credential updated.")
