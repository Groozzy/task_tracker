from classic.http_api import App as BaseApp

from task_tracker.adapters.api import controllers


class App(BaseApp):

    @classmethod
    def create(
        cls,
        tracker: controllers.Tracker,
    ):
        app = cls(prefix='/api')
        app.register(tracker)
        return app
