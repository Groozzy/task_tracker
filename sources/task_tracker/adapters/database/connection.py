from functools import partial

from embrace import pool
import psycopg
import threading

from task_tracker.adapters.database.settings import Settings


class ConnectionHolder(threading.local):
    def __init__(self):
        super().__init__()
        self.connection_pool = pool.ConnectionPool(
            partial(psycopg.connect, Settings.DATABASE_URL),
            limit=10
        )

    def __enter__(self):
        self.connection = self.connection_pool.getconn()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
