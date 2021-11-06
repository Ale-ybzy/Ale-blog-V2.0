use mysql;
-- new user
set password for root@localhost = password('Wl410078368/*');
-- important
grant all on *.* to root@'%' identified by 'Wl410078368/*' with grant option;
-- use privileges
flush privileges;
use ale_blog;