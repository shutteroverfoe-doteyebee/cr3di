import typer
from cr3di.models import Credential
from cr3di.storage import load_credentials, save_credentials

def store(
    username: str = typer.Option(..., "-u", "--username", help="Username"),
    password: str = typer.Option(..., "-p", "--password", help="Password"),
    description: str = typer.Option(..., "-d", "--description", help="Short description"),
    domain: str = typer.Option("", "--domain", "-D", help="Domain (optional)"),
    ip: str = typer.Option("", "--ip", "-i", help="IP address (optional)")
):
    creds = load_credentials()
    new_cred = Credential(username=username, password=password, description=description, domain=domain, ip=ip)
    creds.append(new_cred)
    save_credentials(creds)
    typer.echo(f"[+] Credential for '{username}' saved.")
