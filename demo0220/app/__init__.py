from flask import Flask, request
caches = [] # 数据缓存

app = Flask(__name__)


from .user import user


app.register_blueprint(user, name_prefix="/api") # user related interfaces

@app.route("/")
def entry_main():
    return {"name": "main"}


