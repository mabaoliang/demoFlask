import os, random, string, jsonify

# 定义蓝图
from config.db import db
from models.Classification import Classification
from models.ContentImg import ContentImg
from models.Classification import Classification
from config.codeUtil import model_to_dict, success, fail
import os
import time
from flask import Blueprint, request, send_from_directory
from config import config
# 定义蓝图
from werkzeug.utils import secure_filename

basedir = os.path.abspath(os.path.dirname(__file__))  # 定义一个根目录 用于保存图片用python_sql

imgview = Blueprint('img', __name__, static_folder='static', static_url_path='/static/file')

# 新增
@imgview.route('/add', methods=['GET', "POST"])
def add():
    t = request.values.get('contentTitle')
    img = request.values.get('contentImg')
    cid = request.values.get('forgetId')
    obj = ContentImg()
    obj.contentBrowse = 0
    obj.contentDownload = 0
    obj.contentTitle = t
    obj.contentImg = img
    obj.forgetId = cid
    db.session.add(obj)
    db.session.commit()
    return success()

# 查询
@imgview.route('/select', methods=['GET', "POST"])
def select():
    total = ContentImg.query.count()
    page = request.values.get('page')
    limit = request.values.get('limit')
    if request.values.get('forgetId'):

        cid = request.values.get('forgetId')
        arr = ContentImg.query.filter(ContentImg.forgetId == cid).paginate(page=int(page), per_page=int(limit),
                                                                            error_out=False)
        # arrc = ContentImg.query.filter(ContentImg.forgetId == cid)
        return {"data":model_to_dict(arr.items),"code":1,"total":total,"message":"请求成功"}
    else:
        # arrc = ContentImg.query.filter()
        arr = ContentImg.query.paginate(page=int(page), per_page=int(limit), error_out=False)
        return {"data":model_to_dict(arr.items),"code":1,"total":total,"message":"请求成功"}

# 删除
@imgview.route('/delete', methods=['GET', "POST"])
def delete():
    if request.values.get('contentId'):

        cid = request.values.get('contentId')
        obj = ContentImg.query.filter(ContentImg.contentId == cid).first()
        if obj :
          db.session.delete(obj)
          db.session.commit()
          return success([],'删除成功',1)
        else:
            return fail()
    else:

        return fail()


# 更新下载量 浏览量
@imgview.route('/update',methods=["POST"])
def update():
      cid = request.values.get('contentId')
      obj = ContentImg.query.filter(ContentImg.contentId == cid).first()
      if request.values.get('contentBrowse'):  # 浏览量
          obj.contentBrowse= request.values.get('contentBrowse')


      if request.values.get('contentDownload'):  # 下载量
           obj.contentDownload = request.values.get('contentDownload')

      db.session.commit()

      return  success()


# 下载
@imgview.route('/image/<path:filename>', methods=['GET', 'POST'])
def fileUrl(filename):
    return send_from_directory(config.UPLOAD_FILE, filename)


# 上传
@imgview.route('/upload/<prefix>', methods=['GET', 'POST'])
def upload(prefix):
    file = request.files.get('file')
    print(file)
    filename = secure_filename(str(int(round(time.time() * 1000))) + file.filename)
    # 判断文件是否存在
    if not os.path.exists(config.UPLOAD_FILE + "/" + prefix):
        os.mkdir(config.UPLOAD_FILE + "/" + prefix)
    file.save(os.path.join(config.UPLOAD_FILE, prefix + '/' + filename))
    return success("上传成功！", r'/img/image/' + prefix + '/' + filename)
