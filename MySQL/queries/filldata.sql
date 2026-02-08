use konosuba;
 
 INSERT INTO people (name, age, gender, image_path) VALUES
('Kazuma', 17, 'male', 'uploads/kazuma.jpg'),
('Aqua', 18, 'female', 'uploads/aqua.jpg'),
('Megumin', 14, 'female', 'uploads/megumin.jpg'),
('Darkness', 18, 'female', 'uploads/darkness.jpg'),
('Eris', 18, 'female', 'uploads/eris.jpg'),
('Yunyun', 14, 'female', 'uploads/yunyun.jpg'),
('Wiz', 20, 'female', 'uploads/wiz.jpg'),
('Vanir', 30, 'male', 'uploads/vanir.jpg'),
('Chris', 16, 'female', 'uploads/chris.jpg'),
('Mitsurugi', 18, 'male', 'uploads/mitsurugi.jpg');

INSERT INTO weapons (name, stocks) VALUES
('Chunchunmaru', 1),
('Staff of Agility', 5),
('Cursed Sword', 1),
('Excaliber', 0),
('Holy Dagger', 10);

INSERT INTO purchases (weapon_id, customer_id,total_spent) VALUES
(1, 1,100.23), 
(2, 3,78.75), 
(5, 9,83.01), 
(3, 10,43.93);
UPDATE purchases
SET  total_spent = 88.75
WHERE purchase_id = 2;


INSERT INTO konosuba.purchases 
(weapon_id, customer_id,total_spent) VALUES
(3, 1,100.23), 
(5, 1,78.75), 
(5, 1,83.01),
(2, 1,43.93);

INSERT INTO konosuba.purchases
(weapon_id,customer_id,total_spent)
VALUES 
      (5,1,100),
      (5,1,200),
      (5,1,300);

 -- joins
 /**
 # inner joins
 this joins are created by union two different
 tables that have something in common, based on the keys, primary or foreing key
SELECT * FROM table1
INNER JOIN  table2
ON table1.name = table2.name ;

i guess this "ON" keywords is another filter
it only select the rows that match for both sides. 

LEFT AND RIGHT JOIN  i still dont get it :( 
  */
USE konosuba;

/** 
here i am joining three diffent tables 
where has the 
|no purchase|customer|weapon name|
|---|--|--|
using inner join in order to know 
wich customer bought wich wapon
and that pretty much it 

*/
SELECT 
a.purchase_id as "NO. Purchase" ,
b.name as Customer,
c.name as `Weapon name`
FROM purchases  a
INNER JOIN  people  b
ON 
  a.customer_id = b.people_id
INNER JOIN weapons c
ON
   a.weapon_id = c.weapon_id
ORDER BY b.name desc;
/** 
here using Left join i want to know 
whic people bought a wapon and who doesnt 
*/
Select DISTINCT
  customer.name,
  purchases.purchase_id
From people customer 
LEFT JOIN purchases 
  ON customer.people_id = purchases.customer_id 
ORDER BY customer.name asc ;

/**her i want to know how many the name kazuma appears */
SELECT
  COUNT(purchases.customer_id)
FROM people customer
LEFT JOIN purchases 
    ON customer.people_id = purchases.customer_id 
WHERE customer.name = "Kazuma";

USE konosuba;
SELECT a.name as "Protagonist"
FROM people a
WHERE a.people_id BETWEEN 1 AND 4;

SELECT CONCAT(people_id,". ",name) as Customer,age
FROM people LEFT JOIN purchases 
ON purchases.customer_id = people.people_id;
  

 
SELECT name,image_path FROM people
UNION ALL
SELECT name,weapon_id FROM weapons;

SELecT * from  konosuba.purchases;
SELecT * from  konosuba.weapons;
