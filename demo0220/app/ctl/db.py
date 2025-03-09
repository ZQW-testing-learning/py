# from app.db import get_db

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



if __name__ == "__main__":
    u = Users(name="zqw", age=25, phone="1234567890")
    c = u.create_table({
        "id": "INTEGER PRIMARY KEY",
        "name": "TEXT NOT NULL",
        "phone": "TEXT",
        "department": "TEXT",
        "create_at": "TEXT"
    })
    print(c)