#!/usr/bin/env bash
wget http://repo.mysql.com/mysql-apt-config_0.8.9-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.9-1_all.deb
sudo apt-get update
sudo apt-get install mysql-server
echo "Create holberton_user"
mysql -uroot -p -e "GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn'"
echo "Show holberton_user permissions"
mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"
echo "creating tyrell_corp database"
mysql -uroot -p -e "CREATE DATABASE tyrell_corp;GRANT SELECT ON tyrell_corp.* TO 'holberton_user'@'localhost';FLUSH PRIVILEGES;"
