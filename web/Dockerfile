
# 基础镜像
FROM daocloud.io/python:3.6

# 维护者信息
MAINTAINER maybach
ADD init /usr/src/init

# app 所在目录
WORKDIR /usr/src/init

RUN pip install -r init.txt

WORKDIR /usr/src/myblog

