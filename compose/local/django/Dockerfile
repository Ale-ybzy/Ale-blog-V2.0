FROM python:3.6-alpine

# 设置python环境变量
ENV PYTHONUNBUFFERED 1

RUN apk update \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

# 创建 my_blog 文件夹
RUN mkdir /my_blog

# 将 my_blog 文件夹为工作目录
WORKDIR /my_blog

# 将当前目录内容加入到工作目录中（. 表示当前目录）
ADD . /my_blog

# 利用 pip 安装依赖（- i 表示指定清华源，默认源下载过慢）
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

#设置环境变量
ENV SPIDER=/my_blog

# COPY ./requirements.txt /app/requirements.txt
# RUN pip install -r /app/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

COPY ./compose/local/django/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh