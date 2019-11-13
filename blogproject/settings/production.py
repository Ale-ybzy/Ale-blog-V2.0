from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '(isg8)^y8$3w-tw38_=j9njx+!z6^7b6k$l4*hh)s^o22d0%e-'
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.ybzb.online']  #域名前加点表示允许该域名下的子域名访问

