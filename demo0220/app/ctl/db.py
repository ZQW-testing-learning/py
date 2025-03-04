# from app.db import get_db

class Mode:
    def __init__():
        print('Mode init')

def create_database(tname: str, properties: dict):
    pps = []
    for k, v in properties.items():
        pps.append(f"{k} {v}")
    PPS = ", ".join(pps)
        
    return f'''CREATE TABLE IF NOT EXISTS {tname} ({PPS})'''

def insert(tname: str, **opts: dict):
    fk = ', '.join([k for k in opts.keys()])
    fv = ', '.join([f"'{v}'" if isinstance(v, str) else str(v) for v in opts.values() ])
    return f'''INSERT INTO {tname} ({fk}) VALUES ({fv})'''

def update(tname: str, **opts: dict):
    where = opts.get('where', None)
    ws = []
    # if where is not None:
        
    return f'''UPDATE {tname} SET WHERE '''

if __name__ == "__main__":
    # print(create_database('users', {"id": "INTEGER PRIMARY KEY AUTOINCREMENT", "name": "TEXT", "age": "INTEGER"}))
    print(insert("users", name='zqw', age=25))