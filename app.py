from controller import create_app
from models.test import Test
from configparser import ConfigParser
conf=ConfigParser()
conf.read(r"runningmode.ini",encoding="utf-8")
runnningmode=conf.get("mode","MODE")
app=create_app(runnningmode)


