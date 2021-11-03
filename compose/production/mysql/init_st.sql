USE mysql;
-- new user
set password for root@localhost = password('Wl410078368/*');
-- important
grant all on *.* to root@'%' identified by 'Wl410078368/*' with grant option;
-- use privileges
flush privileges;


-- 建库
create database `ale_blog`;
SET character_set_client = utf8;
USE ale_blog;

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;
