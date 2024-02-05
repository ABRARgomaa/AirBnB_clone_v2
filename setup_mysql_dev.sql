#!/bin/bash

# MySQL credentials
MYSQL_USER="root"
MYSQL_PASSWORD="your_root_password"

# Database and user information
DB_NAME="hbnb_dev_db"
DB_USER="hbnb_dev"
DB_PASSWORD="hbnb_dev_pwd"

# Commands to execute
SQL_QUERY1="CREATE DATABASE IF NOT EXISTS $DB_NAME;"
SQL_QUERY2="CREATE USER IF NOT EXISTS '$DB_USER'@'localhost' IDENTIFIED BY '$DB_PASSWORD';"
SQL_QUERY3="GRANT ALL PRIVILEGES ON $DB_NAME.* TO '$DB_USER'@'localhost';"
SQL_QUERY4="GRANT SELECT ON performance_schema.* TO '$DB_USER'@'localhost';"

# Execute SQL queries
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "$SQL_QUERY1"
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "$SQL_QUERY2"
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "$SQL_QUERY3"
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "$SQL_QUERY4"
