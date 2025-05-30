import os
import json
import gnupg
from openpyxl import Workbook
from rich.console import Console

console = Console()

def export_data():
    gpg = gnupg.GPG()
    CRED_FILE = os.path.expanduser("~/.cr3di/credentials.json.gpg")
    NOTES_FILE = os.path.expanduser("~/.cr3di/notes.json.gpg")
    EXPORT_FILE = os.path.expanduser("~/cr3di_export.xlsx")

    wb = Workbook()
    ws_creds = wb.active
    ws_creds.title = "Credentials"
    ws_notes = wb.create_sheet(title="Secure Notes")

    exported = False

    # Export credentials
    if os.path.exists(CRED_FILE):
        with open(CRED_FILE, "rb") as f:
            decrypted = gpg.decrypt_file(f)
            if decrypted.ok:
                creds_data = json.loads(str(decrypted))
                if creds_data:
                    ws_creds.append(["Username", "Password", "IP", "Domain", "Description"])
                    for cred in creds_data:
                        ws_creds.append([
                            cred.get("username", ""),
                            cred.get("password", ""),
                            cred.get("ip", ""),
                            cred.get("domain", ""),
                            cred.get("description", ""),
                        ])
                    exported = True

    # Export secure notes
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "rb") as f:
            decrypted = gpg.decrypt_file(f)
            if decrypted.ok:
                notes_data = json.loads(str(decrypted))
                if notes_data:
                    ws_notes.append(["Title", "Content", "Timestamp"])
                    for note in notes_data:
                        ws_notes.append([
                            note.get("title", ""),
                            note.get("content", ""),
                            note.get("timestamp", ""),
                        ])
                    exported = True

    if exported:
        wb.save(EXPORT_FILE)
        console.print(f"[green][+] Exported data to:[/green] {EXPORT_FILE}")
    else:
        console.print("[yellow][!] Nothing to export.[/yellow]")
