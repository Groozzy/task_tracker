from datetime import datetime
from typing import Optional

from dataclasses import dataclass


@dataclass
class User:
    id: int
    email: Optional[str] = None


@dataclass
class Task:
    author: User
    title: str
    description: Optional[str] = None
    deadline: Optional[datetime] = None
