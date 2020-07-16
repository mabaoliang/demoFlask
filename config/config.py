import os
SQLALCHEMY_DATABASE_URI = 'mysql://root:12345678@localhost:3306/python_sql'  # localhost
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
JSON_AS_ASCII = False
DEBUG = True
SECRET_KEY = '\x88W\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJJU\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x95*4'
UPLOAD_FILE = os.path.abspath(os.path.dirname(__file__)).split('demoFlask')[0] + 'demoFlask/static/file'  # 定义一个根目录 用于保存图片用'/static/file's
# app screct
LOG = {
    'LEVEL': 'DEBUG',
    'DIR': 'logs',
    'SIZE_LIMIT': 1024 * 1024 * 5,
    'REQUEST_LOG': True,
    'FILE': True,
}
