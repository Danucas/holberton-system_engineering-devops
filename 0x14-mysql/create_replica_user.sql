CREATE USER 'replica_user'@'%' IDENTIFIED BY '1234';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
