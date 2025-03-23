from flask import Blueprint, request, current_app, jsonify
from app.user.control import append_user
from app.user.model import Users
dataCaches = []
user = Blueprint('users', __name__, url_prefix='/api/users')

@user.get("/all")
def get_all_user():
    # all = Users()
    u = Users()
    # u.db.Connect()
    u.create_table({
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT UNIQUE NOT NULL",
        "phone": "TEXT",
        "department": "TEXT",
        "create_at": "TEXT",
        "roles": "TEXT"
    })
    list = u.fetchall()
    u.db.Close()
    return jsonify(list)


@user.post("/add/user")
def add_new_user():
    """
    add one user each time
    """
    oneUser = request.get_json()
    u = Users()
    u.insert(**oneUser)
    u.commit()
    list = u.fetchall()
    u.db.Close()
    return {"data": list}


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


@user.get("/get/user/<int:id>")
def get_user_by_id(id):
    """
    get user by id
    """
    u = Users()
    rows = u.filter(id=id)
    u.db.Close()
    return {"data": rows}
