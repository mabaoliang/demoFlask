import os, random, string,jsonify

from flask import Blueprint, request

# 定义蓝图
from config.db import db
from models.Classification import Classification
from config.codeUtil import model_to_dict, success, fail

basedir = os.path.abspath(os.path.dirname(__file__))  # 定义一个根目录 用于保存图片用

classview = Blueprint('class', __name__)

# 增加
@classview.route('/add',methods=["GET","POST"])
def add():
       name = request.values.get('className')
       c = Classification()
       c.className = name
       db.session.add(c)
       db.session.commit()
       return success([] ,'添加成功', 1)

# 更新
@classview.route('/update',methods=["GET","POST"])
def update():
    cid = request.values.get('classId')
    name = request.values.get('name')
    c = Classification.query.get(cid)
    if c is None:
        return fail([], '没有此数据', -1)
    c.className = name
    db.session.commit()
    return success()


# 查询
@classview.route('/select',methods=['GET','POST'])
def select():
        data=Classification.query.filter(Classification.status==0)
        return success(model_to_dict(data),'请求成功', 1)

# 删除
@classview.route('/delete',methods=["GET","POST"])
def delete():
       cid = request.values.get('classId')
       c = Classification.query.get(cid)
       if c is None:
           return  fail([],'没有此数据',-1)
       c.status=1
       db.session.commit()
       return  success()