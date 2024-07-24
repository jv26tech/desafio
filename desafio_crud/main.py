import os
from pathlib import Path

default_path = Path(os.path.dirname(__file__)).parent
os.chdir(default_path)

from config import Config
from db import Connection, DBBase, DBManager, QueryExecutor
from models import PostModel, UserModel
from scripts import ScriptFillTables, ScriptPost, ScriptSetupDB, ScriptUser


class Main:
    def __init__(self, db: DBBase) -> None:
        self.db = db

    @staticmethod
    def setup():
        tables = [UserModel, PostModel]
        ScriptSetupDB(manager, tables)

    def run(self):
        self.setup()
        ScriptFillTables(self.db)
        ScriptPost(self.db)
        ScriptUser(self.db)


if __name__ == '__main__':
    conn = Connection(Config)
    qe = QueryExecutor(conn)
    manager = DBManager(qe)
    main = Main(manager)
    main.run()
    conn.disconnect()
