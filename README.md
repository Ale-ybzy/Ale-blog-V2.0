# 个人博客 
> 参考自追梦人物博主https://www.zmrenwu.com 的博客教程部署搭建，非常感谢！
django+nginx+gunicorn+mysql架构,博客部署在阿里云服务器,IT小学生正在努力学习中...

## 更新部署
```shell
source venv/bin/activate  #激活虚拟环境(linux)
pip freeze > requirements.txt  #复制本地运行环境
pip install -r requirements.txt  #安装运行环境
git pull #同步代码
python manage_production.py migrate  #迁移数据库
python manage_production.py collectstatic --noinput  #收集静态文件
sudo systemctl restart nginx   #重启nginx服务  
gunicorn blogproject.wsgi -w 2 -k gthread -b 127.0.0.1:8000  #启动应用程序
supervisorctl -c ~/etc/supervisord.conf #进入supervisor控制台，update更新配置，quit推出
```

## https免费证书申请
```shell
sudo yum -y install yum-utils
sudo sudo yum install -y certbot python2-certbot-nginx  #两程序是Let’s Encrypt 提供的 HTTPS 证书申请的工具
sudo certbot --nginx  #运行证书申请命令
#（若有问题执行：
#    bash $ pip uninstall requests $ pip uninstall urllib3 $ yum remove python-urllib3 $ yum remove python-requests
#    bash $ sudo yum install -y certbot python2-certbot-nginx  #重装依赖重装程序）
```
