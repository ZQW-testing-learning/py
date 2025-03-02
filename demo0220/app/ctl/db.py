# from app.db import get_db

def data_to_sql_format(opts: dict):
    for k, v in opts.items():
        if type(opts[k]) == str:
            opts[k] = f'"{v}"'
    return opts



def create_database(tname: str, properties: dict):
    pps = []
    for k, v in properties.items():
        pps.append(f"{k} {v}")
    PPS = ", ".join(pps)
        
    return f'''CREATE TABLE IF NOT EXISTS {tname} ({PPS})'''

def insert(tname: str, opts: dict):
    pps = []
    print("insert...", opts.items())
    for k in opts:
        print('for :', k)
    # for k, v in opts.items():
    #     pps.append()


if __name__ == "__main__":
    # print(create_database('users', {"id": "INTEGER PRIMARY KEY AUTOINCREMENT", "name": "TEXT", "age": "INTEGER"}))
    insert("users", {
        "name": "zqw",
        "age": 25
    })