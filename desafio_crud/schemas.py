from dataclasses import dataclass
from typing import Optional


@dataclass
class UserSchema:
    name: str
    username: str
    email: str
    phone: str
    website: str
    id: Optional[int] = None


@dataclass
class PostSchema:
    title: str
    body: str
    userId: str
    id: Optional[int] = None
