from classic.components import component

from task_tracker.application import services


@component
class Tracker:
    tracker = services.Tracker

    def on_get_show_task(self, request, response):
        task = self.tracker.get_task(**request.params)
        response.media = {
            'author': task.author,
            'title': task.title,
            'description': task.description,
            'deadline': task.deadline,
        }
