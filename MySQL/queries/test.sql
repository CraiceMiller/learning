
-- CREATE DATABASE IF NOT EXISTS Test;
-- DROP DATABASE IF EXISTS Test; 
USE workbench;
CREATE TABLE IF NOT EXISTS workbench.info(
    id INT PRIMARY KEY auto_increment,
    name VARCHAR(10) UNIQUE
);
-- DROP TABLE IF  EXISTS info;

DELETE FROM info 
where id =2;

INSERT INTO info (name)
VALUES
("ashley");

SELECT DISTINCT * FROM info
ORDER BY id desc
-- WHERE id >= 0
LIMIT 100;

