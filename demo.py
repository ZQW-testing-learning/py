import sqlite3
from sqlite3 import Cursor
from abc import ABC, abstractmethod
from typing import Any, Optional
# 数据库基类
class DataBase(ABC):

    __DB__: sqlite3

    def __new__(cls, DB=None, **cfg):
        cls.__DB__ = DB
        return super().__new__(cls)
    
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
    __DB__ = None
    def Connect(self):
        if not self.conn:
            self.conn = Sqlite3.__DB__.connect('test.db')
            self.conn.row_factory = Sqlite3.__DB__.Row
        return self.conn
    
    def Close(self):
        self.closeCursor()
        if self.conn is not None:
            self.conn.close()
            self.conn = None
    
    def Cursor(self):
        if not self.cursor:
            self.cursor = self.conn.cursor()
        return self.cursor
    
    def closeCursor(self):
        if self.cursor is not None:
            self.cursor.close()
            self.cursor = None
        return self.cursor
            

    def start_transaction(self):
        print("start transaction")

    def commit(self):
        print("commit")

    def rollback(self):
        print("rollback")


class Mode:
    def __init__(self, **kwargs):
        self.table_name = self.__class__.get_class_name().lower()
        self.properties = kwargs
        print('Mode init', self.properties)

    def __iter__(self):
        for k, v in self.properties.items():
            yield k, v

    def create_table(self, properties: dict):
        pps = []
        for k, v in properties.items():
            pps.append(f"{k} {v}")
        PPS = ", ".join(pps)
            
        return f'''CREATE TABLE IF NOT EXISTS {self.table_name} ({PPS})'''

    def insert(self, **opts: dict):
        fk = ', '.join([k for k in opts.keys()])
        fv = ', '.join([f"'{v}'" if isinstance(v, str) else str(v) for v in opts.values() ])
        return f'''INSERT INTO {self.table_name} ({fk}) VALUES ({fv})'''

    def update(self, **opts: dict):
        where = opts.get('where', None)
        ws = []
        # if where is not None:
            
        return f'''UPDATE {self.table_name} SET WHERE '''

    @classmethod
    def get_class_name(cls):
        return cls.__name__



class Users(Mode):
    name: str = ''
    age: int = 0
    phone: str = ''
    

d = Sqlite3(sqlite3, user="root")
d.Connect()
cursor = d.Cursor()
user = Users(name="zqw", phone="1234567890", department="技术研发")

sql_create_text = user.create_table({
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "name": "TEXT NOT NULL",
    "phone": "TEXT",
    "department": "TEXT",
    "create_at": "TEXT"
})

sql_text = user.insert({
    "name": "郑泉伟",
    # ""
})

cursor.execute(sql_text)

d.Close()




