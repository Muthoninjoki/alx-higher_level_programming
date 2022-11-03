-- creates MYSQL server user user_0d_1
-- user_0d_1 has all privileges on MYSQL server
-- user_0d_1 password is set to user_0d_1_pwd

CREATE USER
	IF NOT EXISTS 'user_0d_1'@'localhost'
	IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
	ON *.*
	TO 'user_0d_1'@'localhost'
	IDENTIFIED BY 'user_0d_1_pwd';
FLUSH PRIVILEGES;
