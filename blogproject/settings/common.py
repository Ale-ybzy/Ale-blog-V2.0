"""
Django settings for blogproject project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '(isg8)^y8$3w-tw38_=j9njx+!z6^7b6k$l4*hh)s^o22d0%e-'
#
# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
#
# ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.ybzb.online'] #域名前加点表示允许该域名下的子域名访问
#

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'blog.apps.BlogConfig', #注册blog应用
    'comments.apps.CommentsConfig', #注册 comments 应用
    'ckeditor', #注册富文本应用
    'ckeditor_uploader',  #图片上传应用
    'userprofile',  #用户管理
    'accstat',  #访问统计
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blogproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], #os.path.join()函数可将目录和文件合称为一个路径
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blogproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         'OPTIONS':{
#             #'read_default_file': [os.path.join(BASE_DIR, 'venv\my.cnf')],
#             'read_default_file': 'E:\\Python\\Web-Blog\\Ale-blog-2.0\\venv\\my.cnf',
#         },
#     }
#
#
#     # 'substitute': {
#     #     'ENGINE': 'django.db.backends.mysql',
#     #     'NAME': '****',
#     #     'USER': '****',
#     #     'PASSWORD': '****',
#     #     'HOST': '127.0.0.1',
#     #     'PORT': '3306',
#     # }
# }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
# 经测试验证发现True字段的话会导致归档视图月份无法成功过滤
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

#静态文件路径
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#图片上传路径
MEDIA_URL = '/media/'
# 放在django项目根目录，同时也需要创建media文件夹
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
CKEDITOR_UPLOAD_PATH = 'upload/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_FORCE_JPEG_COMPRESSION = True

# ckeditor编辑器配置
CKEDITOR_CONFIGS = {
    # django-ckeditor默认使用default配置
    'default': {
        # 编辑器宽度自适应
        'width':'750px',
        'height':'150px',
        # tab键转换空格数
        'tabSpaces': 4,
        # 工具栏风格
        'toolbar': 'Custom',
        # 添加 Prism 相关插件
        'extraPlugins': ','.join(['codesnippet', 'prism', 'widget', 'lineutils']),
        # 工具栏按钮
        'toolbar_Custom': [
            # 表情 代码块
            ['Smiley', 'CodeSnippet'],
            # 字体风格
            ['Bold', 'Italic', 'Underline', 'RemoveFormat', 'Blockquote'],
            # 字体颜色
            ['TextColor', 'BGColor'],
            # 链接
            ['Link', 'Unlink'],
            # 列表
            ['NumberedList', 'BulletedList'],
            # 最大化
            ['Maximize'],
            # 图片
            ['Image'],
        ],
        # 加入代码块插件
        'extraPlugins': ','.join(['codesnippet']),
    }
}
