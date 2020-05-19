# 在导入app时，django会检查每个在INSTALLED_APPS中的app的default_app_config变量，
# 如果没有设置，django会使用基类AppConfig，因此我们只需要在init.py中指定default_app_config即可

default_app_config = 'accstat.apps.AccstatConfig'