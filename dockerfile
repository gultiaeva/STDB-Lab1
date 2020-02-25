FROM mysql 
ENV MYSQL_ROOT_PASSWORD qwerty123 
ENV POSTGRES_DB library 
COPY library.sql /docker-entrypoint-initdb.d/
