FROM python:3.6-alpine
#声明此镜像基于 python:3.6-alpine 基础镜像构建

ENV PYTHONUNBUFFERED 1
#设置环境变量 PYTHONUNBUFFERED=1

RUN apk update \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

WORKDIR /MyBlog
#创建容器项目目录


COPY requirements /MyBlog/requirements
RUN pip install -r requirements -i https://pypi.douban.com/simple
#容器内安装项目相关依赖软件

COPY . /MyBlog
# 复制当前宿主机下的所有目录文件（除dockerignore中指定的）至容器/app目录下
# 复制启动脚本至容器
COPY ./compose/production/django/start.sh /start.sh

RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh
