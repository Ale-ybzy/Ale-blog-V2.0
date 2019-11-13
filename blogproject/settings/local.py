from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '(isg8)^y8$3w-tw38_=j9njx+!z6^7b6k$l4*hh)s^o22d0%e-'
SECRET_KEY = 'development-secret-key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.ybzb.online'] #域名前加点表示允许该域名下的子域名访问
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'OPTIONS':{
            #'read_default_file': [os.path.join(BASE_DIR, 'venv\my.cnf')],
            'read_default_file': 'E:\\Python\\Web-Blog\\Ale-blog-2.0\\venv\\my.cnf',
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