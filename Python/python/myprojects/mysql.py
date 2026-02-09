import sqlite3 as sql 
import os

class MySQL:

    def createTable(self,path:str,tablename:str,**columns:str)->None:

        if  os.path.exists(path):
            print("The table already exists")
            return 

        if not path.endswith(".db"):
            path = path +".db"


        with sql.connect(path) as connect:
            text='''CREATE TABLE IF NOT EXISTS '''
            
            name= text + tablename+"( "
            col="id INTEGER PRIMARY KEY,\n"
            for key,value in columns.items():
                col+=str(key)+" "+value.upper()+"\n"

            col+= ")"

            text = text+name+col

            cursor=connect.cursor()
            cursor.execute(text)


            """ 

            cursor.execute(
                '''INSERT INTO user (name,age) VALUES (?,?)''',
                ("Craice",19)
            )
            cursor.execute(
                '''INSERT INTO user (name,age) VALUES (?,?)''',
                ("Ashely",17)
            )

            cursor.execute("SELECT * FROM user")
            rows=cursor.fetchall()
            for i in rows:
                print(i)

            """


    def insert(self,path:str,tablename:str,columns:tuple[str,...],_Parameters:tuple):
        with sql.connect(path) as connect: 
            cursor=connect.cursor()

            text='''INSERT INTO ''' + tablename + " " + f"{columns}"+ f" VALUES ({"?,"*len(columns)}) "

            cursor.execute(text, _Parameters)


    def display(self,path:str,tablename:str,):
        with sql.connect(path) as connect: 
            cursor=connect.cursor()

            cursor.execute("SELECT * FROM "+tablename)
            rows=cursor.fetchall()
            for row in rows:
                print(row)
