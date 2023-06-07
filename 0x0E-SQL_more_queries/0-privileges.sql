/*A script shows MySQL server priviledge for user_0d_1 and user_0d_2*/
SELECT CONCAT ('SHOW GRANTS FOR' 'user_0d_1'@'localhost', 'user_0d_2'@'localhost';) FROM mysql.user;
