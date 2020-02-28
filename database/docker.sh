docker stop library || true \
&& docker rm library || true \
&& docker build -f Dockerfile -t library_img . \
&& docker run --name library -p 3306:3306 -d library_img mysqld --lower_case_table_names=1
