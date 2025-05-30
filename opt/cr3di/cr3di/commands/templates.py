import json
import os
import typer
import time
import gnupg
import datetime
import pandas as pd
from rich.console import Console
from rich.table import Table
from cr3di.storage import load_credentials  # to optionally preview usage

console = Console()
gpg = gnupg.GPG()
TEMPLATE_FILE = os.path.expanduser("~/.cr3di/templates.json")



def add_template(
    name: str = typer.Option(..., "-n", "--name", help="Template name"),
    command: str = typer.Option(..., "-c", "--command", help="Command with placeholders")
):
    templates = load_templates()
    templates.append({
        "name": name,
        "command": command,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    })
    save_templates(templates)
    print(f"[DEBUG] Saving template: {name}")
    console.print(f"[DEBUG] Actual path: {TEMPLATE_FILE}")
    console.print(f"[green][+] Template '{name}' saved.[/green]")

def load_templates():
    if not os.path.exists(TEMPLATE_FILE):
        return []
    with open(TEMPLATE_FILE, "rb") as f:
        decrypted = gpg.decrypt_file(f)
        if not decrypted.ok:
            return []
        return json.loads(str(decrypted))


def save_templates(templates):
    data = json.dumps(templates, indent=2)
    recipients = [gpg.list_keys()[0]["uids"][0]]
    encrypted = gpg.encrypt(data, recipients=recipients, always_trust=True)
    if not encrypted.ok:
        raise ValueError("Failed to encrypt templates")
    with open(TEMPLATE_FILE, "wb") as f:
        f.write(encrypted.data)


def list_templates():
    templates = load_templates()
    if not templates:
        console.print("[yellow][!] No templates found.[/yellow]")
        raise typer.Exit()

    table = Table(title="Command Templates")
    table.add_column("Name", style="bold cyan")
    table.add_column("Command", style="white")
    table.add_column("Timestamp", style="dim")

    for tpl in templates:
        table.add_row(tpl["name"], tpl["command"], tpl.get("timestamp", "N/A"))

    console.print(table)


def delete_template(name: str = typer.Option(..., "--name", "-n", help="Template name to delete")):
    templates = load_templates()
    filtered = [tpl for tpl in templates if tpl["name"].lower() != name.lower()]
    if len(filtered) == len(templates):
        console.print(f"[red][!] No template found with name '{name}'[/red]")
        raise typer.Exit()
    save_templates(filtered)
    console.print(f"[green][+] Template '{name}' deleted.[/green]")


def export_templates(output: str = typer.Option("cr3di_templates.xlsx", "--output", "-o", help="Export filename")):
    templates = load_templates()
    if not templates:
        console.print("[yellow][!] No templates to export.[/yellow]")
        raise typer.Exit()
    df = pd.DataFrame(templates)
    df.to_excel(output, index=False)
    console.print(f"[green][+] Templates exported to {output}[/green]")
