USE plushystore; 

DELETE FROM customers
WHERE id = 6;
ALTER TABLE plushystore.customers
CHANGE COLUMN name name VARCHAR(10) UNIQUE NOT NULL; 

ALTER TABLE plushystore.customers
CHANGE COLUMN discount discount DECIMAL(3,2);

ALTER TABLE plushystore.customers
CHANGE COLUMN age age TINYINT;

INSERT INTO plushystore.customers 
(name,age,is_vip,phone_number)
VALUES ("John",34,TRUE,09871234),
		("Veronica",26,FALSE,128930);


UPDATE plushystore.customers
SET discount = 0.70
WHERE is_vip = TRUE 
AND id >0;
ALTER TABLE customers
ADD COLUMN since DATE; 

INSERT INTO customers
(name,age,is_vip,phone_number,since)
VALUES ("sora",18,TRUE,000222,current_date());
-- test 2
-- CONSTRAINT AND CHECK KEYWORDS 
-- constraint make a limitation in certain column
-- and check verify it i guess :(
ALTER TABLE customers 
ADD CONSTRAINT is_adult
 CHECK(age >=18);
 
ALTER TABLE customers
DROP  is_adult;



-- defualt, this keywords will help us to set a determinate value 
-- when we dont add in the inser into statment
-- instead of leave it null, it will be replace by our default value :)
ALTER TABLE customers
CHANGE is_vip is_vip BOOLEAN DEFAULT FALSE;

ALTER TABLE customers
ALTER discount SET DEFAULT 0;

ALTER TABLE customers
ADD COLUMN since_hour
DATETIME ;


INSERT INTO customers(name,age,phone_number,since)
VALUES("CRIS",19,3829102,current_date());
-- end test 2

-- here is where i display all my progress so far :)
-- current table 
-- id, name, age, is_vip, phone_number , discount, since
SELECT *
FROM customers
-- WHERE name LIKE "s%"
ORDER BY id desc 
LIMIT 10;

SELECT VERSION();

