import redis

class BaseSettings:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "onegoNB"
    SESSION_TYPE = 'redis'
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 20


class DevSettings(BaseSettings):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://local:hyf3513SQL@127.0.0.1/local_test"
    DEBUG = True
    SESSION_REDIS = redis.Redis(host='127.0.0.1', port=6379, password="hyf3513REDIS",db=1) # 操作的redis配置


class ProSettings(BaseSettings):
    SQLALCHEMY_TRACK_MODIFICATIONS = ''
    DEBUG = False


settings_map = {
    "develop": DevSettings,
    "product": ProSettings
}

# 配置文件的书写要求
# 可以采用类的方式进行：通用配置 生产环境 开发环境 的继承与重构

# 配置文件必须要有的项
    # SQL类
        # SQLALCHEMY_DATABASE_URI
        # SQLALCHEMY_TRACK_MODIFICATIONS
    # DEBUG
    # Session类
        #SESSION_TYPE
        #SESSION_USE_SIGNER
        #SESSION_TYPE
        #PERMANANT_SESSION_LIFETIME
        #SECRET_KEY



