import typer
from cr3di.commands import store, list_cmd, delete, clear, update, run, notes, templates, export_data

app = typer.Typer(help="cr3di - Encrypted Credential Manager for Pentesters")

app.command("store", help="Store a new credential")(store.store)
app.command("list", help="List stored credentials")(list_cmd.list_creds)
app.command("delete", help="Delete credential by keyword")(delete.delete)
app.command("clear", help="Delete entire credential file")(clear.clear)
app.command("update", help="Update an existing credential using fzf")(update.update)
app.command("run", help="Run a command with {{user}}, {{pass}}, etc. placeholders")(run.run)
app.command("add-note", help="Add a secure note")(notes.add_note)
app.command("list-notes", help="List all secure notes")(notes.list_notes)
app.command("delete-note", help="Delete a note by keyword")(notes.delete_note)
app.command("export-notes", help="Export notes to a spreadsheet")(notes.export_notes)
app.command("add-template", help="Save a command template")(templates.add_template)
app.command("list-templates", help="List all templates")(templates.list_templates)
app.command("delete-template", help="Delete a saved template")(templates.delete_template)
app.command("export-templates", help="Export templates to Excel")(templates.export_templates)
app.command("export", help="Export saved credentials and notes")(export_data.export_data)

if __name__ == "__main__":
    app()
