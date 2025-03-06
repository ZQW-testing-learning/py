import sqlite3, os
from flask import g, Flask

class DataBase:
    def __init__(self, **cfg: dict):
        self.database = cfg.get("database", None)
        self.user = cfg.get("user", 'root')
        self.password = cfg.get("password", None)
        self.port = cfg.get("port", 3306)
        self.conn = None
        self.cursor = None
    
    def Connect(self):
        try:
            if 'db' not in g:
                g.db = sqlite3.connect('test.db')
                g.db.row_factory = sqlite3.Row
                self.conn = g.db
            return self.conn
        except Exception as e:
            self.conn = None
            print("connect database error: ", e)
            return None
    
    def Cursor(self):
        if self.cursor is None:
            self.cursor = self.conn.cursor()
        return self.cursor
    
    def start_transaction(self):
        self.cursor.execute("BEGIN")
    
    def commit(self):
        self.conn.commit()
    
    def rollback(self):
        self.conn.rollback()



def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('test.db')
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app: Flask):
    app.teardown_appcontext(close_db)
