# from app import app
# import bp_manager
import configparser
import click
from app import app
import bp_manager
#编码一个click命令组
@click.group()
def cli():
    pass

#启动服务器
# 参数：mode 启动模式
@click.command()
@click.option("--mode",default="develop",help="Select the running mode",type=click.Choice(["develop","product"]),required=True)
def run_server(mode):
    set_runningmode(mode)
    app.run()
    print("Server is running")
cli.add_command(run_server)


#命令示例
@click.command()
def hello():
    print("hello")
cli.add_command(hello)





# 修改设置文件
def set_runningmode(mode):
    conf=configparser.ConfigParser()
    conf.read(r"runningmode.ini",encoding="utf-8")
    conf.set("mode","MODE",mode)
    try :
        with open(r"runningmode.ini","w",encoding="utf-8") as f:
            conf.write(f)
            f.close()
    except:
        print('ConfigurationFile ERROR T_T')



if __name__=="__main__":
    cli()

#进入一个命令组，方便执行子命令
