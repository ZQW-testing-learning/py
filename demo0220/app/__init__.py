from flask import Flask, request, current_app
caches = [] # 数据缓存

app = Flask(__name__)
print("app path", app.instance_path)

# 初始化数据库
# from . import db

# 注册蓝图
# from user import user
from app.user import user
app.register_blueprint(user) # user related interfaces


@app.route("/")
def entry_main():
    return {"name": "main"}


