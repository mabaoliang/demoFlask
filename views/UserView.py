import os, random, string,jsonify

from flask import Blueprint, request

# 定义蓝图
from config.db import db
from models.User import User
from config.codeUtil import model_to_dict, success, fail, error

basedir = os.path.abspath(os.path.dirname(__file__))  # 定义一个根目录 用于保存图片用

userView = Blueprint('user', __name__)

# 新增用户
@userView.route("/add",methods=['GET','POST'])
def add():
       if(request.method=="GET"):
         {
             print('get')
         }
       user = User()
       data = request.get_json(silent=True)
       print (request.args.get("userName"))
       user.userName = request.args.get("userName")
       user.userPwd = request.args.get("userPwd")
       db.session.add(user)
       db.session.commit()
       return '------'

# 查询用户
@userView.route("/select",methods=['GET','POST'])
def select():

       stus = User.query.filter().all()
       return success(model_to_dict(stus))

# 删除
@userView.route('/delete',methods=['GET','POST'])
def delete():
     id = request.values.get('userId')
     user =User.query.filter(User.userId==id).first()
     db.session.delete(user)
     db.session.commit()
     return success()

# 登录
@userView.route('/login',methods=["POST"])
def login():
       if(request.method=="POST"):
           account = request.values.get('userName')
           pwd = request.values.get("userPwd")
           # 查询总条数
           total = User.query.filter(User.userAccount==account,User.userPwd==pwd).count()
           if(total==1):
                  user=User.query.filter(User.userAccount==account,User.userPwd==pwd)
                  return success(model_to_dict(user))
           else:

              return fail()
       else:
         return  error()


# def way(n):
#     if n < 2:
#         return 1
#     else:
#         return n * way(n - 1)
#
# if __name__ == '__main__':
#     print("开始计算。。。")
#     print(way(6))
#     print("计算结束！")

