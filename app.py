from flask import Flask, render_template
from config.app import create_app

app = create_app()


# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     return render_template("index.html")



# 主函数
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True)
