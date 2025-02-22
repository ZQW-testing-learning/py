from flask import Flask, request
caches = [] # 数据缓存

app = Flask(__name__)

@app.route("/")
def entry_main():
    return {"name": "main"}


@app.route("/user/all")
def get_user_detail():
    return caches

def append_user(user: dict):
    """
    append user to list
    """
    item = None
    if len(caches) > 0:
        ids = map(lambda n: n["id"], caches)
        maxId = max(ids)
        item = dict(**user, id=maxId+1)
        caches.append(item)
    else:
        item = dict(**user, id=1)
        caches.append(item)
    return item


@app.post("/add/user")
def add_new_user():
    """
    add one user each time
    """
    user = request.get_json()
    item = append_user(user)
    print("body", user)
    return {"data": item["id"]}


@app.post("/add/users/batches")
def add_users_batches():
    """
    add users in batches
    """
    usersBatches = request.get_json()
    users = usersBatches.get("users", [])
    startIndex = 0
    isLen = len(users)
    appendIds = []
    if isLen > 0:
        while startIndex < isLen:
            item = append_user(users[startIndex])
            appendIds.append(item["id"])
            startIndex += 1
    print('users', users)
    return {"data": appendIds}


