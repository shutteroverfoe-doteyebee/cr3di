import subprocess
import typer
from rich.console import Console
from cr3di.storage import load_credentials, load_templates
from InquirerPy import inquirer
import pty
import shlex


console = Console()

def run(template: str = typer.Option(None, "-t", "--template", help="Run from a saved template"),
         command: list[str] = typer.Argument(None, help="Command to run with placeholders")):

    creds = load_credentials()
    if not creds:
        console.print("[red][!] No stored credentials.[/red]")
        raise typer.Exit()

    # Prompt for credential selection
    cred_labels = [f"{c.username} ({c.description})" for c in creds]
    selected = inquirer.select(
        message="Select credential:",
        choices=cred_labels
    ).execute()
    index = cred_labels.index(selected)
    cred = creds[index]

    # Load command from template or argument
    if template:
        templates = load_templates()
        match = next((t for t in templates if t["name"] == template), None)
        if not match:
            console.print(f"[red][!] Template '{template}' not found.[/red]")
            raise typer.Exit()
        cmd = match["command"]
    elif command:
        cmd = " ".join(command)
    else:
        console.print("[red][!] No command or template provided.[/red]")
        raise typer.Exit()

    # Substitute placeholders
    final_cmd = (
        cmd.replace("{user}", cred.username)
           .replace("{pass}", cred.password)
           .replace("{ip}", cred.ip or "")
           .replace("{domain}", cred.domain or "")
    )

    console.print(f"[blue][+] Running:[/blue] {final_cmd}")


    try:
        console.print("[blue][+] Launching interactive shell...[/blue]")
        pty.spawn(shlex.split(final_cmd))
    except Exception as e:
        console.print(f"[red][!] Error: {e}[/red]")
    finally:
        os.system("stty sane")
        console.print("[green][+] Terminal restored.[/green]")

