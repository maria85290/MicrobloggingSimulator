# Microblogging Environment Simulator

 
We present a platform that simulates social media microblogging, inspired by the Twitter layout, with the aim of creating an environment where social media-focused studies can be conducted without compromising ethical values.  The end result is a platform tested in a lab environment with the ability to present the content (in the format of post) to validate or investigate and record user interactions.

###  To use the platform, you can follow the next steps:

1. Download this repository.
Execute:
2. docker-compose up -d --build
3. docker cp populate.sql simulator_mysql:/populate.sql
4. docker exec -it simulator_mysql /bin/bash -c "mysql -u root -p123456789 twitter_env < populate.sql"
5. Access the web application page: http://127.0.0.1:8000;

