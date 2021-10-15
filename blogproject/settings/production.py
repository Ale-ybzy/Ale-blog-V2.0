from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(isg8)^y8$3w-tw38_=j9njx+!z6^7b6k$l4*hh)s^o22d0%e-'


# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = False
DEBUG = False

ALLOWED_HOSTS = ['*']  #域名前加点表示允许该域名下的子域名访问
# ALLOWED_HOSTS = ['.ybzb.online', '127.0.0.1']  #域名前加点表示允许该域名下的子域名访问

#数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'OPTIONS': {
        #     'read_default_file': '/home/Ale/etc/my.cnf',
        # },
        'HOST': 'blog_mysql',  # 容器名称
        'NAME': 'ale_blog',  # 数据库名称
        'USER': 'root',
        'PASSWORD': 'Wl410078368/*',
        'PORT': '13306',
        'OPTIONS': {'charset': 'utf8mb4'},

    }
}
