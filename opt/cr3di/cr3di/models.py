from typing import Optional
from pydantic import BaseModel

class Template(BaseModel):
    name: str
    command: str

class Credential(BaseModel):
    username: str
    password: str
    description: str
    domain: Optional[str] = ""
    ip: Optional[str] = ""
