from config.app import create_app

"""
    建表工具类

    ！如果需要重新生成 必须删除数据库对应模型生成的表
"""

# 需要导入那些模型就加那些模型
from config.db import db
from models.User import User


app = create_app()
with app.app_context():
    db.create_all()
