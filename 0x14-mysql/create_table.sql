CREATE DATABASE IF NOT EXISTS tyrell_corp;
GRANT SELECT ON tyrell_corp.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6(
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255) NOT NULL
);
INSERT INTO nexus6(name)
VALUES('Leo');
