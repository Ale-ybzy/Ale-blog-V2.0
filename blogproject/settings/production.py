from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '(isg8)^y8$3w-tw38_=j9njx+!z6^7b6k$l4*hh)s^o22d0%e-'
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.ybzb.online']  #域名前加点表示允许该域名下的子域名访问

#数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'OPTIONS':{
            #'read_default_file': [os.path.join(BASE_DIR, 'venv\my.cnf')],
            'read_default_file': '/etc/mysql/my.cnf',
        },
    }


    # 'substitute': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': '****',
    #     'USER': '****',
    #     'PASSWORD': '****',
    #     'HOST': '127.0.0.1',
    #     'PORT': '3306',
    # }
}
