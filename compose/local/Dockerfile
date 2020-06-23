FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

WORKDIR /app
COPY requirement.txt /app/requirement.txt
RUN pip install -r requirement.txt -i https://pypi.douban.com/simple
COPY ./compose/local/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh