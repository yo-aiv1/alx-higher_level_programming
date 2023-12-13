-- create new user in the current server
CTEATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1';i
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
