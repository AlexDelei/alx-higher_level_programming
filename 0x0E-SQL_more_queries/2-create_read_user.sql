-- Creating a database and a user


-- Creating the database even if it exists
CREATE DATABASE hbtn_0d_2;

-- Creating user if does not exists and grants privileges
CREATE USER  'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT  ON hbtn_0d_2.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;
