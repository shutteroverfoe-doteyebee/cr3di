# cr3di 🧠🔐

**Encrypted Credential CLI for Pentesters and Red Teamers**

Securely store, view, update, and inject credentials into tools like `evil-winrm`, `crackmapexec`, etc. using placeholders like `{{user}}`, `{{pass}}`, `{{domain}}`, and `{{ip}}`.

## 🚀 Features

- 🔐 GPG-encrypted JSON credential storage
- 🔍 Search, update, or delete credentials
- 🧠 Auto placeholder replacement in commands
- ⚡️ Fast selection using `fzf`
- 🧹 Restores terminal after broken tools

## 📦 Installation

### Option 1: Install from `.deb`

sudo dpkg -i cr3di-deb.deb

### Option 2: Manual

git clone https://github.com/YOUR_USERNAME/cr3di.git
cd cr3di
pip install -r requirements.txt

Then run:
PYTHONPATH=. python3 -m cr3di --help

## 🔧 Usage

cr3di store -u bob -p hunter2 -d "Main Admin"
cr3di list
cr3di run -- evil-winrm -u {{user}} -p {{pass}} -i {{ip}}


## 📜 License

MIT

### 📜 3. `requirements.txt`

typer[all]
rich
pydantic
python-gnupg
