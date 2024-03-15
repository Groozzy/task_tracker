from task_tracker.adapters import api

from task_tracker.composites.container.container import container


api = container.resolve(api.App)

if __name__ == '__main__':
    from werkzeug import run_simple

    run_simple('127.0.0.1', 9000, api)
