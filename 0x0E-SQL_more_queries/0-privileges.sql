/*A script that creates the MySQL server user user_0d_1 */
SELECT CONCAT('SHOW GRANTS FOR \'', user, '\'@\'localhost\';') AS grant_query
FROM mysql.user
WHERE user IN ('user_0d_1', 'user_0d_2');
