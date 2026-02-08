-- this action only modify the column,value of a the rows
-- that meets the condition where
USE plushystore;
SET SQL_SAFE_UPDATES =1;
UPDATE customers
SET is_vip = TRUE, 
    phone_number = 12345789
WHERE name = "Craice" ;

INSERT INTO customers(name,is_vip,phone_number)
VALUES ("Sthepahny",TRUE,09865432);




ALTER TABLE customers
ADD COLUMN discount  DECIMAL(3,2);

UPDATE customers
SET discount = 0.70
WHERE is_vip =TRUE;
-- this action delete the entire row 
-- based on the filter where
DELETE FROM customers
WHERE id =  7;

ALTER TABLE  customers
ADD COLUMN age INT(2)
AFTER name;
-- my attempts
UPDATE customers
set age=19
where id =1 OR id= 3;

UPDATE customers
set age=20
where id=2;
UPDATE customers 
set name = "Ashley",
    age = 18
WHERE id=4;

UPDATE customers
set age=21
where id=5;
-- end of the atempts hre :(
/*
--based on the internet resource
-- with AUTOCOMMIT, all the data for now on
-- will not save automatly
-- we manually need to save it
my best anolygy for this one, this acts symylary like commit in git, or the
save progress button in our favorite games. it save all our data in a determinate
state. if we messed up, or die in our game we easely can play again. but lossing the progress we need 
untill our last save. 
we only need to type 
COMMIT,
and if we die, then type, our checkpoint :),
ROLLBACK
*/
SET AUTOCOMMIT = OFF;
-- SAVE our progress in our game :)
USE plushystore;
COMMIT;
-- IF WE RUN THIS IT WILL DELETE ALL OUR ROWS :O
DELETE FROM customers
WHERE id >0;
-- therefore, this will lost forever, i guess :o
INSERT INTO customers (name,age,is_vip,phone_number)
VALUES ("Very important person",40,TRUE,6666999);

-- revive again from our last checkpoint;
ROLLBACK;
-- display our table
SELECT * FROM customers
-- WHERE phone_number IS NOT NULL AND is_vip = TRUE
ORDER BY name asc
LIMIT 10;