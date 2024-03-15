from typing import Optional

from classic.components import component
import embrace

from task_tracker.application import interfaces, entities
from task_tracker.adapters.database.connection import ConnectionHolder


@component
class UsersRepo(interfaces.UsersRepo):
    connection_holder: ConnectionHolder
    queries: embrace.Module

    @property
    def connection(self):
        return self.connection_holder

    def get_by_email(self, email: str) -> Optional[entities.User]:
        return self.queries.users.select_by_email(self.connection, email)

    def add(self, user: entities.User):
        self.queries.users.insert(self.connection, **user.)  # Посмотреть метод для получения только атрибутов as_dict()


@component
class TasksRepo(interfaces.TasksRepo):
    connection_holder: ConnectionHolder
    queries: embrace.Module

    def add(self, task: entities.Task):
        self.queries.tasks.insert(self.connection, task)

    def remove(self, task: entities.Task):
        self.queries.tasks.delete(self.connection, task)
