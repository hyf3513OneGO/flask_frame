from app import app


#引入蓝图
from controller.hello.route_hello import bp_hello
from controller.picAPI.picapi import picapi




#注册蓝图
app.register_blueprint(bp_hello,url_prefix="/hello")
app.register_blueprint(picapi,url_prefix="/picapi")

