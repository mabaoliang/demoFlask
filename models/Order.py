from config.db import db


class Order(db.Model):

    # 数据库的表名
    __tablename__ = 'py_order'
    # 单个属性 对应数据库中的列 db.BigInteger 为列的类型此列为bigint,primary_key为主键
    orderId = db.Column(db.BigInteger, primary_key=True)

    # 状态
    status = db.Column(db.Integer, unique=False)

    # 用户 openid
    openid = db.Column(db.String(255), unique=False)

    # money 金额
    money = db.Column(db.String(255), unique=False)

    # time  创建时间
    createTime = db.Column(db.DateTime, unique=False, default=db.Datetime.now)

    # 产品Id
    contentId = db.Column(db.BigInteger, db.ForeignKey('py_content.contentId'))
