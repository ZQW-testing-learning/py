# import sqlite3, os
# from flask import g, Flask

# def get_db():
#     if 'db' not in g:
#         g.db = sqlite3.connect('test.db')
#         g.db.row_factory = sqlite3.Row
#     return g.db


# def close_db(e):
#     db = g.pop('db', None)
#     if db is not None:
#         db.close()

# def init_app(app: Flask):
#     app.teardown_appcontext(close_db)


import sqlite3
from sqlite3 import Cursor
from abc import ABC, abstractmethod
from typing import Any, Optional
from datetime import datetime
# 数据库基类
class DataBase(ABC):

    __DB__: Optional[sqlite3.Connection] = None
    
    def __init__(self, DB=None, **cfg: dict):
        self.database = cfg.get("database", None)
        self.user = cfg.get("user", 'root')
        self.password = cfg.get("password", None)
        self.port = cfg.get("port", 3306)
        self.conn = None
        self.cursor: Cursor | None = None
    
    @abstractmethod
    def Connect(self):
        '''
        连接数据库
        '''
        pass

    @abstractmethod
    def Close(self):
        '''
        关闭数据库连接
        '''
        pass
    
    @abstractmethod
    def Cursor(self):
        '''
        数据库游标
        '''
        pass
    
    @abstractmethod
    def start_transaction(self):
        '''
        开启数据库事务
        '''
        pass
    
    @abstractmethod
    def commit(self):
        '''
        提交事务
        '''
        pass
    
    @abstractmethod
    def rollback(self):
        '''
        回滚事务
        '''
        pass


class Sqlite3(DataBase):

    def Connect(self):
        if not self.conn:
            print("database connection...")
            self.conn = sqlite3.connect(self.database)
            self.conn.row_factory = sqlite3.Row
        else:
            print("use old connection")
            self.conn = None
        return self.conn
    
    def Close(self):
        self.closeCursor()
        if self.conn is not None:
            self.conn.close()
            self.conn = None
            print("close connection")
        return self.conn
    
    def Cursor(self):
        if not self.cursor:
            print("create new cursor")
            self.cursor = self.conn.cursor()
        else:
            print("use old cursor")
        return self.cursor
    
    def closeCursor(self):
        if self.cursor is not None:
            self.cursor.close()
            self.cursor = None
            print("close cursor")
        return self.cursor
            

    def start_transaction(self):
        cur = self.Cursor()
        cur.execute("BEGIN TRANSACTION")
        print("start transaction")

    def commit(self):
        self.conn.commit()
        print("commit")

    def rollback(self):
        self.conn.rollback()
        print("rollback")


class Mode:
    def __init__(self, **kwargs):
        self.db = Sqlite3(sqlite3, user="root", database="../test.db")
        self.conn = self.db.Connect()
        self.table_name = self.__class__.get_class_name().lower()
        self.properties = kwargs

    def __iter__(self):
        for k, v in self.properties.items():
            yield k, v


    def start_transaction(self):
        self.db.start_transaction()
    
    def commit(self):
        self.db.commit()
    
    def rollback(self):
        self.db.rollback()

    def create_table(self, properties: dict):
        pps = []
        for k, v in properties.items():
            pps.append(f"{k} {v}")
        PPS = ", ".join(pps)
        cur = self.db.Cursor()
        cur.execute(f'''CREATE TABLE IF NOT EXISTS {self.table_name} ({PPS})''')
        print("create table ok")


    def insert(self, **opts: dict):
        fk = ', '.join([k for k in opts.keys()])
        fv = ', '.join([f"'{v}'" if isinstance(v, str) else str(v) for v in opts.values() ])
        cur = self.db.Cursor()
        cur.execute(f'''INSERT INTO {self.table_name} ({fk}) VALUES ({fv})''')
        print("insert ok")

    def update(self, **opts: dict):
        where = opts.get('where', None)
        ws = []
        return f'''UPDATE {self.table_name} SET WHERE '''
    
    def fetchall(self):
        cur = self.db.Cursor()
        cur.execute(f'''SELECT * FROM {self.table_name}''')
        rows = cur.fetchall()
        print('fetchall ok')
        return [dict(row) for row in rows]
    
    def filter(self, **opts: dict):
        fields = list(opts.keys())
        values = [f"'{v}'" if isinstance(v, str) else str(v) for v in opts.values()]
        conditions = [f"{k}={v}" for k, v in zip(fields, values)]
        where = ' AND '.join(conditions)
        cur = self.db.Cursor()
        cur.execute(f'''SELECT * FROM {self.table_name} WHERE {where}''')
        rows = cur.fetchall()
        return [dict(row) for row in rows]
    
    def LIKE(self, field: str, mode: str):
        return f"{field} LIKE '{mode}'"
    def WHERE(self, field: str, value: str):
        return f"{field}='{value}'"
        

    @classmethod
    def get_class_name(cls):
        return cls.__name__
