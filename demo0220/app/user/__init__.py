from flask import Blueprint, request, current_app
from .control import append_user
from app.db import get_db
dataCaches = []
user = Blueprint('user', __name__, url_prefix='/user')

@user.get("/all")
def get_all_user():
    db = get_db()
    print(db.execute)
    return dataCaches


@user.post("/add/user")
def add_new_user():
    """
    add one user each time
    """
    oneUser = request.get_json()
    item = append_user(oneUser, dataCaches)
    print("body", oneUser)
    return {"data": item["id"]}


@user.post("/add/batches")
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
            item = append_user(users[startIndex], dataCaches)
            appendIds.append(item["id"])
            startIndex += 1
    print('users', users)
    return {"data": appendIds}
