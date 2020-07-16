from config.db import db

class ContentImg(db.Model):

    # 数据库的表名
    __tablename__ = 'py_content'
    # 单个属性 对应数据库中的列 db.BigInteger 为列的类型此列为bigint,primary_key为主键
    contentId = db.Column(db.BigInteger, primary_key=True)

    # 标题
    contentTitle = db.Column(db.String(255), unique=False)

    # 浏览量
    contentBrowse = db.Column(db.Integer, unique=False)

    # 下载量
    contentDownload = db.Column(db.Integer, unique=False)

    # 壁纸
    contentImg = db.Column(db.String(255), unique=False)

    # 外键
    forgetId = db.Column(db.BigInteger, db.ForeignKey('py_class.classId'))

