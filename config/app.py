from flask import Flask, request, g

from config.db import db



"""
    蓝图-模块化解决方案
    需要register_blueprint注册使用
"""

#
def register_blueprints(app):
     from views.UserView import userView

#     # 注册使用蓝图
     app.register_blueprint(userView, url_prefix="/user")


# 获取app(避免上下文)
def create_app(register_all=True):
    app = Flask(__name__, static_folder='../static', template_folder="../static")
    app.config.from_pyfile("config.py")

    if register_all:
        register_blueprints(app)
        # apply_cors(app)
        db.init_app(app)

    return app