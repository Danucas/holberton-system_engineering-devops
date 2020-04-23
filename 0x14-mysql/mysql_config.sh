#!/usr/bin/env bash
wget http://repo.mysql.com/mysql-apt-config_0.8.9-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.9-1_all.deb
sudo apt-get update
sudo apt-get install mysql-server
mysql -uroot -p -e "CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';"
