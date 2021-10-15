FROM nginx:1.17.1

RUN rm /etc/nginx/conf.d/default.conf

COPY ./compose/production/nginx/blog_nginx.conf /etc/nginx/conf.d/blog_nginx.conf