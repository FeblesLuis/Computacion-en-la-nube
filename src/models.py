from pydantic import BaseModel
from typing import List

class DirectoryItem(BaseModel):
    id: int
    path: str
    name: str
    emails: List[str]
