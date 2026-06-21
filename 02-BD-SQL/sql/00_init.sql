
CREATE ROLE student WITH LOGIN PASSWORD 'postgresqldksl';

CREATE DATABASE practice_db OWNER student;


GRANT ALL PRIVILEGES ON DATABASE practice_db TO student;

