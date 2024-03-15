import logging

from classic.container import container, factory, instance
from classic.operations import Operation
import embrace

from task_tracker import application
from task_tracker.adapters import database, api


container.register(
    application,
    database,
    api,
)


logging.basicConfig(level=logging.INFO)


def new_operation(connection_holder: database.ConnectionHolder) -> Operation:
    return Operation(
        context_managers=connection_holder,
    )


container.add_settings({
    embrace.Module: instance(embrace.module(database.SQL_DIR)),
    database.ConnectionHolder: instance(database.ConnectionHolder),
    Operation: factory(new_operation),
    api.App: factory(api.App.create),
})
