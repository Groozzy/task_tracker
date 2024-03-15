from datetime import datetime

from classic.components import component
from classic.operations import operation
from pydantic import BaseModel

from . import entities, interfaces


class TaskInfo(BaseModel):
    author: entities.User
    title: str
    description: str
    deadline: datetime


@component
class Tracker:
    tasks: interfaces.TasksRepo

    @operation
    def add_task(self, task_info: TaskInfo):
        task = task_info.model_construct(entities.Task)  # TODO: implement pydantic
        self.tasks.add(task)
