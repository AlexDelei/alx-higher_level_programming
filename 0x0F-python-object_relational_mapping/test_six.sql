-- Database + tables to test
DROP DATABASE IF EXISTS test_6;
CREATE DATABASE IF NOT EXISTS test_6;
USE test_6;

CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
