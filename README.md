# **CR3DI** 🧠🔐
## *Encrypted Credential, Notes & Command Templates CLI for Pentesters and Red Teamers*

*Securely store, view, update, and inject credentials or pre-created command templates into tools like evil-winrm, crackmapexec, etc. using placeholders like {{user}}, {{pass}}, {{domain}}, and {{ip}}. Also, store,view, update and export pentesting notes and findings into excel spreadsheet*

------------


###  Features🚀
- 🔐 GPG-encrypted JSON credential storage
- 🔍 Search, update, or delete credentials
- 🧠 Auto placeholder replacement in commands
- ⚡️ Fast selection using fzf
- 🧹 Restores terminal after broken tools

------------

------------




#### 1. Installation  📦

##### As Debian package (Recommanded)
```bash
git clone https://github.com/shutteroverfoe-doteyebee/cr3di.git
```
```bash
cd cr3di/
```
```bash
sudo chmod +x build.sh 
```
```bash
sudo chmod +x DEBIAN/postinst DEBIAN/control
```
```bash
sudo ./build.sh
```
```bash
cd ..
```
```bash
sudo apt install ./cr3di_xxxxxxx.deb
```
**Recommended : refresh your terminal or just exit it and open it again** 

```bash
gpg --full-generate-key
```
- Press Enter twice
- Press y
- Enter Any name
- Enter Any  Email 
- Press Enter
- Enter O
- Type Your Password & Confirm it --> **You will need this password to encrypt & decrypt your credentials database** :smile: 

------------

------------

#### 2. Usage Examples 🔧


- **--help** : *Purpose: Display usage information for any command*

	Example:
```bash
cr3di store --help
```
```bash
cr3di run --help
```

- **store** - *Purpose : Add a new credential securely*

	*Arguments:*
	|  Argument |   Required   | Description  |
	| ------------ | ------------ | ------------ |
	| -u, --username  |✅ Yes   |The username to store   |
	| -p, --password  |✅ Yes   | The password associated with the user  |
	| -d, --description  | ✅ Yes  |Optional description (e.g. "Admin account")   |
	| -D, --domain  |❌ No   | Optional domain name  |
	| -i, --ip  |❌ No   | Optional IP address  |

	*Example:*

```bash
cr3di store -u bob -p hunter2 -d "Main Admin" -D example.com -i 192.168.1.10
```

------------


- **list** - *Purpose : View stored credentials*

	*Arguments:*
	None

	*Example:*
```bash
cr3di list
```

------------


- **delete** <keyword> - *Purpose : Delete credentials that match a keyword (case-insensitive)*

	*Arguments:*
	Argument	Required	Description
	keyword	✅ Yes	Matches against username, domain, or description

	*Example:*
```bash
cr3di delete bob
```

------------


- **update** - *Purpose : Update an existing stored credential*

	*Arguments:*
	No arguments; the tool will display a list of stored credentials, allow you to select one, 		and prompt you to change any fields.

	*Example:*
```bash
cr3di update
```

------------


-  **run** -- <command> : *Purpose: Run any command with credentials injected via placeholders*

	*Arguments:*
	*Placeholder	Description*
	**{user}**	Replaced with the selected username
	**{pass}**	Replaced with the selected password
	**{domain}**	Replaced with the selected domain (if any)
	**{ip}**	Replaced with the selected IP (if any)



   **You must include     - - before the command to separate arguments.**
	*Example:*
   ```bash
   cr3di run -- evil-winrm -u {user} -p {pass} -i {ip}
   ```

   ```bash
   cr3di run -- evil-winrm -u {user} -p {pass} -i 192.168.10.10
   ```

   **OR**

   **You can create a command template and run it**

	*Example:*
   ```bash
   cr3di run -t evil-winrm
   ```
   **In the above example we're assuming that the stored command template is : "evil-winrm -u {user} -p {pass} -i {ip}"**
   
   **Check the templates part for more examples and info** 

   **Remember, You are free to use any number of combos of the above *"run"* 	arguments as long as they are stored in cr3di**
	

------------

- **add-template** - *Purpose: Save a command template for repeated use with injected credentials*

	*Arguments:*
	| Argument | Required | Description |
	|----------|----------|-------------|
	| -n, --name | ✅ Yes | Template name |
	| -c, --command | ✅ Yes | Command with placeholders like {{user}}, {{pass}}, etc. |

	*Example:*
```bash
cr3di add-template -n evil-winrm -c "evil-winrm -u {user} -p {pass} -i {ip}"
```

- **list-templates** - *Purpose: View all saved command templates*

	*Example:*
```bash
cr3di list-templates
```

- **delete-template** - *Purpose: Delete a specific command template*

	*Arguments:*
	| Argument | Required | Description |
	|----------|----------|-------------|
	| -n, --name | ✅ Yes | Name of the template to delete |

	*Example:*
```bash
cr3di delete-template -n evil-winrm
```

------------

- **add-note** - *Purpose: Add a new secure note*

	*Arguments:*
	| Argument | Required | Description |
	|----------|----------|-------------|
	| -t, --title | ✅ Yes | Title of the note |
	| -c, --content | ✅ Yes | Note content |

	*Example:*
```bash
cr3di add-note -t "IP Disclosure" -c "IP is discloused in a txt file: 192.168.1.1"
```

------------

- **list-notes** - *Purpose: View stored secure notes*

	*Example:*
  
```bash
cr3di list-notes
```

------------

- **delete-note** - *Purpose: Delete a secure note*

	*Arguments:*
	No arguments; you will be prompted to select the note.

	*Example:*
  
```bash
cr3di delete-note
```

------------

- **export** - *Purpose: Export all decrypted credentials and notes into an Excel spreadsheet (useful for pentest reporting)*

	*Example:*
```bash
cr3di export
```

------------


- **clear** : *Purpose: Deletes the encrypted credentials file (~/.creds.enc.json.gpg)*

	*Example:*
```bash
cr3di clear
```
------------

------------



#### 3. License 📜

**MIT License**

**Copyright (c) 2025 ShutterOverFoe**

*Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.*

------------

------------


#### 4. Requirements 📜

1. typer[all] 
2. pydantic 
3. python-gnupg
4. InquirerPy

