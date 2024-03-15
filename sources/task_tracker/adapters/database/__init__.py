import pathlib

from .settings import Settings
from .connection import ConnectionHolder


SQL_DIR: pathlib.Path = pathlib.Path(__file__).parent.joinpath('sql')
