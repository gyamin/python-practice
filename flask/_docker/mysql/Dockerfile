FROM mysql:8.0

# ENV設定
ENV MYSQL_ROOT_USER root
ENV MYSQL_ROOT_PASSWORD root-pass
ENV MYSQL_DATABASE flask
ENV MYSQL_USER admin
ENV MYSQL_PASSWORD admin-pass
ENV TZ Asia/Tokyo

# 設定ファイルコピー
COPY ./mysql_project.cnf /etc/mysql/conf.d/mysql_project.cnf

# csvファイルコピー
COPY csv/KEN_ALL_UTF8.CSV /tmp/KEN_ALL_UTF8.CSV

# 起動時実行ファイルコピー
COPY sql /docker-entrypoint-initdb.d