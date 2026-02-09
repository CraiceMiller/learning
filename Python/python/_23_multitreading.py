import threading as th
import time as t
from typing import overload,Self, Any, override
from datetime import datetime
from concurrent.futures import (ThreadPoolExecutor, as_completed)
List= list[str]
    # 2. Learning Overloading same funtions 
    #3. Learning Thread 
    #4. Learning ->Self
    #5. Nested funtions
class Greet:

        NAME:str="Assistance Helper"

        def helper(self, name:str="User")->Self: 
            print(f"Hello {name}, I'm going to help you today")
            return self

        @overload 
        def greet(self, name:str,age:int,/)->None:
            ...

        @overload
        def greet(self, inforamtion:dict,/)->None:
            ...


        def greet(self, *args)->None:
            t.sleep(3)
            hour= datetime.now().hour
            text:str=" "

            if hour >5 and hour <12:
                text = "Good Moring!"
            elif hour >12 and hour < 18: 
                text = "Good Afternoon!"
            else: 
                text ="Good Night!" 

            if (len(args)==2) and (isinstance(args[0],str)) and (isinstance(args[1],int)):
                name, age = args
                text += f" {name} Nice to meet you, You are {age} years olds"
                
            elif len(args) == 1 and isinstance(args[0], dict):
                information = args[0]
                values = " ,".join([str(x) for x in information.values()])
                text += f" {values}"

            print(text)
            



        @staticmethod 
        def work(name:str,*,profession:str,years:int,company:str)->None: 
            t.sleep(6)

            print(f"Hello {name}, You work at {company} as a {profession} during {years} years")

        @staticmethod
        def likes(*likes)->None:
            t.sleep(10)

            print("you like: ")
            for i in likes: 
                t.sleep(0.10)
                print("- ",i)
            print("_"*15)

        @staticmethod 
        def friends(num_friends:int|None=None)->None:
            t.sleep(2)
            if num_friends is None: 
                print("You Dont have any friends :( ")
                return 
            
            print(f"You have {num_friends} friends :)")

        @staticmethod
        def additems(items:List,*args:str)->List:
            new_items=items.copy()
            for i in args: 
                t.sleep(0.40)
                new_items.append(i)
            print("Everything is Done")

            return new_items


        @overload
        def yourfriends(self,*friends:str)->tuple[str,...]:
            """If you use position arguments"""
            ...
        
        @overload
        def yourfriends(self,**friends)->dict[str,Any]:
            """If you use key arguments"""
            ...

        def yourfriends(self,*friends,**friends_dict): 
            """Main Logic"""
            t.sleep(5)

            if isinstance(friends, tuple) and friends != (): 
                print("Your friends: ")
                for names in friends: 
                    print("-", names)
                return friends
            
            if isinstance(friends_dict, dict ) and friends_dict != {}:
                print("Your friends: ")

                my_dict:dict[str,list[Any]]={}

                for key,value in friends_dict.items(): 
                    print(f"{key} | {value}")
                    my_dict[key] = ["Hello",value] 
                return my_dict
    
            return  None
            
        @classmethod
        def givename(cls)->str:
            return cls.NAME




learn="""
#26/08/2025
f1= th.Tread()
    target: is the main purspose of the object, this is the funition we want to run 
    args: This must be a tuple of positional arguments fo the funtion we provide early 
    kwargs: This must be Mapping (a dictionary i guess). This will pass the key as the 
    keyargument and the value as the value of the parameter. 

        We cannot write args and kwargs if the funtion doesnt need. 
            >>> def greet()->None: 
                    ...

    the parameter args is useful if we have funtion that have positional arguments only: 
            >>> def greet(name,age,/)->None: 
                    ...

    Likewise we use the parameter kwargs if we have a funtion that have key arguments only
            >>> def greet(*,name,age)->None: 

    Moreover we can use both (args and kwargs ) when the funtion has position and key argumentes 
            >>> def greet(name,*,age,city,language)->None: 

We use the .start() method to indeed run the funtion. 
f1.start()

Nevertheless I have Three questions: 
    if the funtion return a value, where is it stored ?
        >>> def gree(name,age,/)->str: 

    And What is the differente between run and start method 
    I Dont got it what timeout means neither .join() metods

"""




    # 1.  Lerning Type Alias

if __name__ =='__main__': 

    name:str="Craice"
    likes:list=["Play video games","Study langagues","Hangout with friends","Father's food"]

    #6. learining threding 

    greet=Greet()
    start=t.perf_counter()



    """
    #Normal Threading 
    threads:set=set()



    for _ in range(0): 
        t1=th.Thread(target=greet.greet,args=(name,18),name="Gretting")
        t1.start()

        t2=th.Thread(target=greet.additems,args=(likes, "Coding","drawing","Sleep","Work"))
        t2.start()

        t3=th.Thread(target=greet.likes,args=("Play video games","Study langagues","Hangout with friends"))
        t3.start()

        t4=th.Thread(target=greet.work, args=(name,),kwargs={'profession':"Acconter","years":4,"company":"BankOunt"})
        t4.start()
        t5=th.Thread(target=greet.friends, kwargs={"num_friends":10})
        t5.start()

        threads.add(t1)
        threads.add(t2)
        threads.add(t3)
        threads.add(t4)
        threads.add(t5)



    for thread in threads: 
        thread.join()
        

    """



    #More efficiency threadding
    with ThreadPoolExecutor() as executor:
        my_dict_ls=[{'name':"hersy","age":18},{'name':"Craice","age":19},{'name':"Ashely","age":17}]



        results= [executor.submit(greet.yourfriends,"Hersy","Craice","Ashley") for _ in range(25)]
        f6 = executor.submit(greet.work, "Ashley",profession="Seler",years=3,company="Fruty-Jelly. S.A.")
        f7= executor.submit(greet.givename)

        result2= executor.map(greet.greet,my_dict_ls)





        f6.result()
        print(f7.result())

        value=None
        for f in as_completed(results):
            value=f.result()

        for r in result2: 
            r

        print(value)










    finish=t.perf_counter()

    print("Everything Done!")
    print("Finished in: ",  round(finish - start,2), " seconds")



