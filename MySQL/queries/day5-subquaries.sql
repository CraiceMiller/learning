/**
Subqueries are just queries from 
another querie. 
since our select keyword return a new 
table where our condition. that means we can use that 
result too from another query. 

in other programing languages could a "variable"
where we storage the value and use it later. 
```python
def get_age(name:str)->int: 
    ...

def get_ids()->list[int]:
    ...

def get_table()->list: 
    ...

age:int = get_age("Kazuma")
table = get_table()
ids = get_ids()

for n in table: 
    if n >= age: 
      print(n)

for n in table:
    if n in ids:
        print(n)

```

therefore i see subqueries like function to storage in 
one variable :), where can return one single
value or an array of them, based on my anoly
  

 */
USE konosuba;
SELECT name, age 
FROM people
WHERE age >= (
    -- this  hole query only return one result
    SELECT DISTINCT age 
    FROM people
    WHERE people.name = "Kazuma"
)
ORDER BY name asc;
-- but what about when return more than one value :

-- this is the same. but   is stick with 17
SELECT name,age 
FROM people 
WHERE age >=17;
 
-- here i want to see only the weapon that are 
-- not buy yet
Select CONCAT(weapon_id," ", name) as Weapon
FROM weapons
WHERE weapon_id  IN (
    -- for me this return an array,column, of VALUEs
    -- for this int values :)
    SELECT weapon_id FROM purchases
)
ORDER BY weapon_id;

SET @target_age = 1;
SELECT * FROM  people  
WHERE age >=@target_age
ORDER BY people_id desc;

USE konosuba;
ALTER TABLE konosuba.purchases 
(customer_id,weapon_id,total_spent)
VALUES
(1,2,200),
(1,5,400),
(1,3,700)
;
CREATE VIEW IF NOT EXISTS purchase_summary AS
SELECT 
    customer.name as "Customer",
    w.name as "Weapon",
    p.purchase_time as "Transation day"
FROM 
    purchases AS p
RIGHT JOIN 
     people as customer 
ON 
    p.customer_id = customer.people_id
LEFT JOIN 
    weapons as w
ON 
    p.weapon_id = w.weapon_id
ORDER BY   
    customer.name ASC
;

