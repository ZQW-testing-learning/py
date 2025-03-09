import sqlite3, os
from flask import g, Flask

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
