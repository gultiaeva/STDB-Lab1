FROM mysql:8.0.19

ENV MYSQL_ROOT_PASSWORD=qwerty123
ENV MYSQL_DATABASE=library

COPY scripts/library.sql /docker-entrypoint-initdb.d/

EXPOSE 3306
