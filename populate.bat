docker cp populate.sql simulator_mysql:/populate.sql
docker exec -it simulator_mysql /bin/bash -c "mysql -u root -p123456789 twitter_env < populate.sql"
