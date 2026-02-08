--  over from zero, the goal is to reach until the last line
-- USE plushystore;
DROP TABLE IF  EXISTS  customers;
-- creating the table, columns
CREATE TABLE IF NOT EXISTS customers(
    id INT PRIMARY KEY AUTO_INCREMENT, 
    NAME_OF_THE_CUSTOMER_AT_HAND VARCHAR(100)
);

-- adding a new row
ALTER TABLE customers
ADD COLUMN is_vip Boolean;
-- chaing the name of a column 
ALTER TABLE customers
CHANGE COLUMN NAME_OF_THE_CUSTOMER_AT_HAND name VARCHAR(100) NOT NULL;

-- creating the rows
INSERT INTO customers (name,is_vip )
VALUES
("hersy",FALSE),
("Craice",TRUE)
;
INSERT INTO customers(name,is_vip )
VALUES(
  "Miseru",
  FALSE
 );
 ALTER TABLE customers
 ADD COLUMN phone_number INTEGER ;

INSERT INTO plushystore.customers (name,is_vip,phone_number ) 
VALUES
("Stephany",false,6644663);
-- DISPLAYING OUR DATA
SELECT DISTINCT  *
FROM plushystore.customers
GROUP BY name DESC
LIMIT 10;


/**
it works however i dunno why. I am going to be honest with you my dear friends. the thing is 
i download this vscode extension `database client jdbc` and i do the following: 
name: LearningMySQL
server type:MySQL
host: locolhost
port: 3306
username:root 
password: the same i wrote when i set my password in the mysql sever 
dabatse: null
path:null
and then i conntected it and it works. 
then in appears me this structure: 
LearningMySQL/
   -security/
      -users/
         -root@
   -mysql/
   -plushystore/
   -test/
     -query/
     -tables/
     -views/
     -functions/
     -procedures/
then i create my own database call "plushystore". 
---

then i download this another one "sql tools" where i create this another one: 
connection name: LEARNING-DATA-BASE
sever addres:3306
databse:exampledb
username: CraiceMiller
connection timeout:2000
password: same here, the samein mysql sever

and then it create me antoher sever i guess. and the structure in this another one is 
LEARNING-DATA-BASE/
    -plushystore/
        -tables/
        -views/

and in my vscode setting.json, i have this 
"sqltools.connections": [

        {
            "mysqlOptions": {
                "authProtocol": "default",
                "enableSsl": "Disabled"
            },
            "ssh": "Disabled",
            "previewLimit": 50,
            "server": "127.0.0.1",
            "port": 3306,
            "driver": "MySQL",
            "name": "LEARNING-DATA-BASE",
            "database": "plushystore",
            "username": "root",
            "connectionTimeout": 2000,
            "password": ""
        }

what do you recoomend to do :(, sorry i got i mess here 

*/


