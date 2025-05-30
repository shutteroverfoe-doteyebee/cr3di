import json
import os
from typing import List
from cr3di.models import Credential, Template
import gnupg

gpg = gnupg.GPG()

CRED_FILE = os.path.expanduser("~/.cr3di/credentials.json.gpg")
TEMPLATE_FILE = os.path.expanduser("~/.cr3di/templates.json")
NOTES_FILE = os.path.expanduser("~/.cr3di/notes.json")

def load_credentials() -> List[Credential]:
    if not os.path.exists(CRED_FILE):
        return []
    with open(CRED_FILE, "rb") as f:
        decrypted = gpg.decrypt_file(f)
    if not decrypted.ok:
        raise ValueError("Failed to decrypt credentials.")
    return [Credential(**entry) for entry in json.loads(str(decrypted))]

def save_credentials(creds: List[Credential]):
    data = json.dumps([cred.dict() for cred in creds], indent=2)
    recipients = [gpg.list_keys()[0]["uids"][0]] if gpg.list_keys() else []
    encrypted_data = gpg.encrypt(data, recipients=recipients, always_trust=True)
    if not encrypted_data.ok:
        raise ValueError("Failed to encrypt credentials.")
    os.makedirs(os.path.dirname(CRED_FILE), exist_ok=True)
    with open(CRED_FILE, "wb") as f:
        f.write(encrypted_data.data)

def load_templates() -> List[dict]:
    if not os.path.exists(TEMPLATE_FILE):
        return []
    with open(TEMPLATE_FILE, "rb") as f:
        decrypted = gpg.decrypt_file(f)
    if not decrypted.ok:
        raise ValueError("Failed to decrypt templates.")
    try:
        return json.loads(str(decrypted))
    except json.JSONDecodeError:
        return []

def save_templates(templates: List[dict]):
    data = json.dumps(templates, indent=2)
    recipients = [gpg.list_keys()[0]["uids"][0]] if gpg.list_keys() else []
    encrypted_data = gpg.encrypt(data, recipients=recipients, always_trust=True)
    if not encrypted_data.ok:
        raise ValueError("Failed to encrypt templates.")
    os.makedirs(os.path.dirname(TEMPLATE_FILE), exist_ok=True)
    with open(TEMPLATE_FILE, "wb") as f:
        f.write(encrypted_data.data)

def clear_credentials():
    if os.path.exists(CRED_FILE):
        os.remove(CRED_FILE)

def clear_templates():
    if os.path.exists(TEMPLATE_FILE):
        os.remove(TEMPLATE_FILE)

def clear_notes():
    if os.path.exists(NOTES_FILE):
        os.remove(NOTES_FILE)
