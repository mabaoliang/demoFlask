from config.db import db

class Classification(db.Model):

    # 数据库的表名
    __tablename__ = 'py_class'
    # 单个属性 对应数据库中的列 db.BigInteger 为列的类型此列为bigint,primary_key为主键
    classId = db.Column(db.BigInteger, primary_key=True)

    # 名称
    className = db.Column(db.String(255), unique=False)

    # 状态
    status = db.Column(db.Integer, default=0, unique=False)