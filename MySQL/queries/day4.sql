-- 2026-02-02 at 13:00hrs. 
SET AUTOCOMMIT = OFF; 
CREATE DATABASE IF NOT EXISTS konosuba ; 

USE konosuba; 
DROP TABLE if EXISTS  people,weapons;
CREATE TABLE IF NOT EXISTS people(
    people_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, 
    name VARCHAR(50) NOT NULL,
    age TINYINT(2),
    gender ENUM("male","female"),
    image_path VARCHAR(100) UNIQUE 
);

CREATE TABLE IF NOT EXISTS weapons (
    weapon_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, 
    name VARCHAR(20) NOT NULL UNIQUE ,
    stocks  INT UNSIGNED   DEFAULT 0
)

drop table   IF   EXISTS purchases;

CREATE TABLE IF NOT EXISTS konosuba.purchases(
    purchase_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    purchase_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    customer_id INT UNSIGNED NOT NULL, 
    weapon_id INT UNSIGNED NOT NULL, 
    
    quantity INT UNSIGNED DEFAULT 1,
    total_spent DECIMAL(10, 2) NOT NULL, -- e.g., 999.50 gold
    
    FOREIGN KEY(customer_id) REFERENCES people(people_id),
    FOREIGN KEY(weapon_id) REFERENCES weapons(weapon_id)
);

IF TABLE purchases EXISTS COMMIT;


SELECT * FROM konosuba.purchases 
LIMIT 100 ;