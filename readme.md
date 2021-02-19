#目录结构说明
## config 存储配置文件
## controller 存储蓝图与复用的函数
    __init__.py进行了db初始化，app设置读取，session配置
## models存储数据模型
## static存储静态资源
## templates 存储模板

# 文件用途说明
## manager.py为启动命令行管理器
    run_server --mode develop|product
## app.py对app对象进行初始化
## bp_manager.py为蓝图管理器，蓝图在其中进行引入与注册
## runningmode.ini存储运行模式

