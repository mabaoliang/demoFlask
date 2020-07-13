from config.db import db


class User(db.Model):

    # 数据库的表名
    __tablename__ = 'py_user'
    # 单个属性 对应数据库中的列 db.BigInteger 为列的类型此列为bigint,primary_key为主键
    userId = db.Column(db.BigInteger, primary_key=True)

    # 姓名
    userName = db.Column(db.String(255), unique=False)

    # 密码
    userPwd = db.Column(db.String(255), unique=False)

    # 用户头像
    userPhoto = db.Column(db.String(255), unique=False)

    # 帐号
    userAccount = db.Column(db.String(255), unique=False)
