from typing import Optional, Tuple

from abc import ABC, abstractmethod
from .entities import User, Task


class UsersRepo(ABC):
    @abstractmethod
    def get_by_email(self, email: str) -> User: ...

    @abstractmethod
    def add(self, user: User): ...

    def get_or_create(self, email: Optional[str]) -> Tuple[User, bool]:
        if email:
            if user := self.get_by_email(email):
                return user, False
            user = User(email=email)
        else:
            user = User()
        self.add(user)
        return user, True


class TasksRepo(ABC):
    @abstractmethod
    def add(self, task: Task): ...

    @abstractmethod
    def remove(self, task: Task): ...
