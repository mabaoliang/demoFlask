import os, random, string, jsonify

# 定义蓝图
from config.db import db

from models.ContentImg import ContentImg
from models.Order import  Order
from config.codeUtil import model_to_dict, success, fail
import os
import time
from flask import Blueprint, request, send_from_directory
from config import config
# 定义蓝图
from werkzeug.utils import secure_filename

basedir = os.path.abspath(os.path.dirname(__file__))  # 定义一个根目录 用于保存图片用python_sql

orderView = Blueprint('order', __name__)

# 新增订单
@orderView.route('/add',methods=["POST"])
def add():

    return success()


# 修改订单
@orderView.route('/update',methods=["POST"])
def update():
    return success()


# 查询订单
@orderView.route('/select' ,methods=["get ,post"])
def select():

    return success()

# 删除

@orderView.route('/delete', methods=['post'])
def delete():
      cid =  request.values.get('orderId')
      obj=Order.query.filter(Order.orderId == cid).first()
      obj.delete=1
      db.session.commit()
      return success()