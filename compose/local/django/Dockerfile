FROM python:3.7
# 设置python环境变量
ENV PYTHONUNBUFFERED 1

# 更新基础软件环境
RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev -y

# 创建 my_blog 文件夹
RUN mkdir /my_blog

# 将 my_blog 文件夹为工作目录
WORKDIR /my_blog

# 将当前目录内容加入到工作目录中（. 表示当前目录）
ADD . /my_blog

# 更新 pip
RUN pip install pip -U

# 利用 pip 安装依赖（- i 表示指定清华源，默认源下载过慢）
ADD requirements /my_blog/
RUN pip install -r ./requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

# COPY ./start.sh /start.sh
# RUN sed -i 's/\r//' /start.sh
# RUN chmod +x /start.sh
