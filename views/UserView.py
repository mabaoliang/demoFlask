import os, random, string,jsonify

from flask import Blueprint, request

# 定义蓝图
from config.db import db
from models.User import User
from config.codeUtil import model_to_dict

basedir = os.path.abspath(os.path.dirname(__file__))  # 定义一个根目录 用于保存图片用

userView = Blueprint('user', __name__)

# 新增用户
@userView.route("/add",methods=['GET','POST'])
def add():
       user = User()
       data = request.get_json(silent=True)
       print (request.args.get("userName"))
       user.userName = request.args.get("userName")
       user.userPwd = request.args.get("userPwd")
       db.session.add(user)
       db.session.commit()
       return '------'

# 新增用户
@userView.route("/select",methods=['GET','POST'])
def select():
       stus = User.query.filter().all()
       print(stus)
       for i in stus:
              print(i)
       return {"data":model_to_dict(stus)}
