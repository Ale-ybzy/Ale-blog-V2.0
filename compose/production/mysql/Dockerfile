FROM mysql:5.7

#设置工作目录,/docker-entrypoint-initdb.d目录允许扩展名为.sh, .sql and .sql.gz的文件放入其中。
#如果是.sh则直接执行
#如果是.sql则自动被mysql自行导入
#.sql.gz文件则会先被解压，然后再被导入
WORKDIR /docker-entrypoint-initdb.d
ENV LANG=C.UTF-8

#将当前目录的init.sql文件复制到容器中的以上目录中,init脚本专门用来控制执行sql顺序的，此目录放置多个sql文件的话执行顺序无法保证容易出错
ADD ./compose/local/mysql/init.sql /docker-entrypoint-initdb.d


