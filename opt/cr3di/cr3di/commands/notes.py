import json
import os
import typer
import gnupg
import datetime
import pandas as pd
from rich.table import Table
from rich.console import Console

console = Console()
gpg = gnupg.GPG()
NOTES_FILE = os.path.expanduser("~/.cr3di/notes.json.gpg")


def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "rb") as f:
        decrypted = gpg.decrypt_file(f)
        if not decrypted.ok:
            return []
        return json.loads(str(decrypted))


def save_notes(notes):
    data = json.dumps(notes, indent=2)
    recipients = [gpg.list_keys()[0]["uids"][0]]
    encrypted = gpg.encrypt(data, recipients=recipients, always_trust=True)
    if not encrypted.ok:
        raise ValueError("Failed to encrypt notes")
    with open(NOTES_FILE, "wb") as f:
        f.write(encrypted.data)


def add_note(title: str = typer.Option(..., "--title", "-t", help="Note title"),
             content: str = typer.Option(..., "--content", "-c", help="Note content")):
    notes = load_notes()
    note = {
        "title": title,
        "content": content,
        "timestamp": datetime.datetime.now().isoformat()
    }
    notes.append(note)
    save_notes(notes)
    console.print(f"[green][+] Note '{title}' added.[/green]")


def list_notes():
    notes = load_notes()
    if not notes:
        console.print("[yellow][!] No notes found.[/yellow]")
        raise typer.Exit()

    table = Table(title="Stored Notes")
    table.add_column("Title", style="bold cyan")
    table.add_column("Content", style="white")
    table.add_column("Timestamp", style="dim")

    for note in notes:
        table.add_row(note["title"], note["content"], note["timestamp"])
    console.print(table)


def delete_note(title: str = typer.Option(..., "--title", "-t", help="Title of the note to delete")):
    notes = load_notes()
    filtered = [n for n in notes if n["title"].lower() != title.lower()]
    if len(filtered) == len(notes):
        console.print(f"[red][!] No note found with title '{title}'[/red]")
        raise typer.Exit()
    save_notes(filtered)
    console.print(f"[green][+] Note '{title}' deleted.[/green]")


def export_notes(output: str = typer.Option("cr3di_notes.xlsx", "--output", "-o", help="Export filename")):
    notes = load_notes()
    if not notes:
        console.print("[yellow][!] No notes to export.[/yellow]")
        raise typer.Exit()
    df = pd.DataFrame(notes)
    df.to_excel(output, index=False)
    console.print(f"[green][+] Notes exported to {output}[/green]")
