import typer
from cr3di.storage import load_credentials, save_credentials

def delete(keyword: str = typer.Argument(..., help="Keyword to match username or description")):
    creds = load_credentials()
    filtered = [c for c in creds if keyword.lower() not in c.username.lower() and keyword.lower() not in c.description.lower()]
    if len(filtered) == len(creds):
        typer.echo("[!] No matching entries found.")
        return
    save_credentials(filtered)
    typer.echo(f"[+] Deleted credentials matching '{keyword}'.")
