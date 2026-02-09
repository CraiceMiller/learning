#classes_to_use.py
# object = A "bundle" of related attribures (varialbles) and methods (funtions)
from exercise_8 import Student, Employee #type: ignore
from My_Classes import my_mini_store #type: ignore
from _collections_abc import Iterable,Callable #type: ignore
from iterables_to_use import Currency_,sentences #type: ignore
import random as r 
from typing import Any
from datetime import datetime 
from time import sleep
from math import sqrt
from fractions import Fraction
from collections import defaultdict
from typing import Any, Hashable,Mapping,Self,Tuple
from itertools import zip_longest






#
class Car:
    def __init__(self,
                  model:str,
                  year:int,
                  color:str,
                  for_sale:bool,
                  country:str="USA") -> None:
        
        self.model = model 
        self.year = year
        self.color = color 
        self.for_sale = for_sale
        self.country = country
        self.turn_on=False
        self.is_drive = False
        return 
    
    def show_state(self)->None:
        print(f"model: {self.model}")
        print(f"year: {self.year}")
        print(f"color: {self.color}")
        print(f"is for sale: {self.for_sale}")
        print(f"country: {self.country}")
        print(f"is turn on: {self.turn_on}")
        return 
    
    def drive(self):
        if not self.turn_on:
            print("you need to turn on the car first")
            return 
        
        self.is_drive= True 
        print(f"you're driving the {self.model}")
        return 
    
    def turn_on_car(self):
        if self.turn_on:
            print(f"{self.model} is already turn on")
            return 
        
        self.turn_on= True
        print(f"{self.model} is turn on now...")
        return 
    
    def stop(self):
        if not self.is_drive or not self.turn_on:
            print(f"{self.name} is not driving")
            return 
        
        self.is_drive = False
        print(f"{self.model} has stopped ")
        return 
    
    def turn_off_car(self):
        if not self.turn_on or self.is_drive:
            print("you can't turn off the car")
            return 
        
        self.turn_on = False
        print(f"{self.model} has turned off...")   
#_i.py
class ToDoList:
    def __init__(self,name="User") -> None:
        self.is_complete = [True,True, False, False]
        self.importance = ["High","High","Low","Medium"]
        self.tasks = ["To breath", "To learn python", "To wath anime","To study math"]
        self.name = name

    def show_tasks(self)->None:
        num = 1
        for complet,task,imp in zip(self.is_complete, self.tasks,self.importance):
            print(f"{num}.{task:<20}: {"Complet" if complet else "Incomplet"}{imp:>15}")
            num +=1
        

    def add_task(self,new_tastk,urgency="Medium")->None:
        self.tasks.append(new_tastk)
        self.is_complete.append(False)
        self.importance.append(urgency)
        

    def complet_task(self,num)->None:
        index = num -1

        if self.is_complete[index]:
            print("you already complete that task")
            return 
        
        self.is_complete[index] = True 
        

    def delate_task(self,num)->None:
        index = num -1
        try:
            self.tasks.pop(index)
            self.is_complete.pop(index)
        except IndexError:
            print("you don't have that task...")

    def modify_importance(self,num,urgency)->None:
        index = num -1

        try:
            if urgency == 1:
                self.importance[index] = "Low"
            elif urgency == 2:
                self.importance[index] = "Medium"
            elif urgency == 3:
                self.importance[index] = "High"
            else:
                return None 
                
            
            
        except IndexError:
            print("you don't have that task...")


#r.py
class PersonalityPersonalAssistance:
    """This are class variable for the class"""

   

    ASSISTANCE_NAME:str = 'ChatBot'
    ASSISTANCE_LIKES:list=['help','sleep','do things', 'write']
    random_sentences:tuple = sentences

    @classmethod
    def presentation(cls)->None:
        """This class method only say hello!"""
        print(f"\nHello I'm {cls.ASSISTANCE_NAME}")

    @classmethod
    def speak(cls):
        print(f"{cls.ASSISTANCE_NAME} says: {r.choice(cls.random_sentences)}")

    @staticmethod
    def give_hour():
        print(f"\nToday is ")

         
class PersonalAssistance():
    Time_user_call:int=0
    def __init__(self,
                 extra_info:dict[Any,Any] |None=None,
                 age:int|None=None,
                 is_student:bool|None=None,
                 likes:tuple|list|None=None,
                 name:str|None=None,
                 height:float|None=None,
                 weight:float|None=None,
                 gender:str|None=None,
                 ) -> None:
        """This only storage the basic information of the user"""

        self.name:str|None = name.capitalize() if name is not None else None
        self.likes:tuple|list|None=likes
        self.age:int|None=age
        self.is_student:bool|None=is_student
        self.height:float|None=height
        self.weight:float|None=weight
        self.gender:str|None=gender
        self.extra_info:dict[Any,Any] |None=extra_info

        
        self.is_adult:bool|None=age >=18 if age is not None else None
        

        PersonalAssistance.Time_user_call += 1
        return 
    
    def display_information(self)->None:
        info_given:tuple=(self.age,self.likes,self.name,self.is_student,
               self.height,self.weight,self.gender,self.extra_info,self.is_adult)
        
        if  all(info_given):
            print("The current user doesn't have any information")
            return 

        """This will only create a list of the info give it.."""
        print("-"*30+ f"Basic info of {self.name}"+ "-"*30)
        print()

        if self.name is not None:
            print(f"Name: {self.name:<10}")
        if self.gender is not None:
            print(f"Gender: {self.gender}")
        if self.age is not None:
            print(f"Age: {self.age:<10}")
        if self.is_student is not None:
            print(f"Student: {"Yes" if self.is_student else "No":<10}")
        if self.height is not None: 
            print(f"Height: {self.height:<10}")
        if self.weight is not None: 
            print(f"Weight: {self.weight:<10}")
        if self.likes is not None:
            if isinstance(self.likes, Iterable):
                for value in self.likes:
                    print(f"-{value}")
                print(f'{self.name} likes {len(self.likes)} things')
        
        if  self.extra_info is not None:
            print("\nExtra Information " + "*"*20)
            for index,(key,value) in enumerate(self.extra_info.items(),1):
                if isinstance(value,Iterable):
                    print(f"{index}. {key}:")
                    for i, thing in enumerate(value,1):
                        print(f"- {thing}")
                else:
                    print( f"{index}. {key}: {value}")


#          
class MyCalculator:
    def __init__(self,
                 x:int|float=0,
                 y:int|float=0) -> None:
        self.x=x
        self.y=y
    
    def addtion(self)->int|float:
        """This only return the sum of two numbers: .x + self.y"""
        return self.x + self.y
    
    def subtraction(self)->int|float:
        """This only return the subtraction of two numbers: self.x - self.y"""
        return self.x - self.y
    
    def multiplication(self)->int|float:
        """This only return the multiplication of two numbers: self.x * self.y"""
        return self.x * self.y
    
    def division(self)->int|float|None:
        """This only return the division of two numbers: self.x / self.y
        Return None if you try divide by zero
        """
        if self.y == 0:
            return None
        return self.x / self.y
    
    @staticmethod
    def converter_celsius(num:int|float)->int|float:
        return (num-32)/1.8

    @staticmethod
    def body_mass_index(weight:int|float,
                        height:int|float)->int|float:
        return weight / (height**2)

    @staticmethod
    def  pythagorean_theorem(a:int|float,
                            b:int|float)->float:
        c=sqrt((a**2)+(b**2))
        return c 


    @staticmethod
    def quadratic_formula(a:int|float,
                        b:int|float=0,
                        c:int|float=0
                        )->tuple:
        discriminant=(b**2)-4*a*c
        denominador=2*a


        if discriminant ==0:
            x1=(-b + sqrt(discriminant)) / denominador
            return (x1,0)

        if discriminant >0:
            x1=(-b + sqrt(discriminant)) / denominador
            x2=(-b - sqrt(discriminant)) / denominador

            return (round(x1,3),round(x2,3))
        
        else:
            #i need to ajust this but later... 
            real_part = -b / denominador
            imaginary_part_numerator = sqrt(-discriminant)
            imaginary_part = imaginary_part_numerator / denominador

            root1 = Fraction(int(-b), int(denominador))
            root2 = complex(denominador, imaginary_part_numerator)
            return (root1, root2)
        
    @staticmethod
    def currency_to_dollars(currency:str,
                        amount:int|float)->int|float:
        if not currency in Currency_:
            print("sorry, but we don't have that value")
            return amount
        
        dollars=  amount / Currency_[currency] 

        return round(dollars,2)

    @staticmethod
    def dollars_to_currency(currency:str,
                            dollars:int|float)->int|float:
        if not currency in Currency_:
            print("sorry, but we don't have that value")
            return dollars
        
        currency_change=   Currency_[currency] * dollars

        return round(currency_change,2)

    def calculate_area(self)->float|int:
        """This only will give us the  area"""
        return self.x * self.y

    
class Fruit:
    def __init__(self,name:str,grams:float) -> None:
        self._name=name
        self._grams=grams

    def __str__(self) -> str:
        return f'Name: {self._name}'

    def __eq__(self, __value: object) -> bool:
        return self.__dict__ == __value.__dict__
    
    def __format__(self, __format_spec: str) -> str:
        match __format_spec:
            case 'kg':
                return f'{self._grams/1000:.2f}kg'
            case 'desc':
                return f'{self._name} has {self._grams}g'
            case _:
                return 'Unkwon format specifier...'
    
    def __lt__(self,__value)->bool:
        return self._grams < __value._grams
    
    def __gt__(self,__value)->bool:
        return self._grams > __value._grams
    
    def __add__(self,__value)->int|float:
        return self._grams + __value._grams

    def __or__(self, __value: Any):
        new_name:str=f"{self._name} and {__value._name}"
        new_grams:float=self._grams + __value._grams
        return Fruit(name=new_name, grams=new_grams)
    
    def __repr__(self) -> str:
        return f'Fruit( name={self._name}, grams={self._grams})'
    
    def __getitem__(self,key:str)->str:
        if key == 'name':
            return self._name
        if key == 'grams':
            return str(self._grams)
        return 'N/A'




class Bank:
    
    def __init__(self,
                 balance:float|int=0,
                 wallet:float|int=0,
                 name:str="user",
                 debt:float|int=0) -> None:
        
        self.balance=balance
        self.debt=debt
        self.wallet=wallet
        self.name=name

        self.greet()
        

    def greet(self):
        print(f"Grettings {self.name}!")
        return

    def show_state(self):
        print("____your current status_____")
        if self.debt > 0:
            print(f"{self.balance= :,.2f}")
            print(f"{self.wallet= :,.2f}")
            print(f"{self.debt= :,.2f}")
            print("\n")
            
            return 
        print(f"{self.balance= :,.2f}")
        print(f"{self.wallet= :,.2f}")
        print("\n")
        return 

    def withdraw(self,):
        if self.balance <= 0:
            print("INSUFECENT FOUNDS!!!!")
            return 
        
        print("how many do you want withdrawn...")
        amount = None
        while amount is None:
            try :
                validing_amount=float(input())

                if validing_amount > self.balance:
                    print("you can't withdrawn money that you don't have!!")
                    continue 

                if validing_amount <=0:
                    print("it must be greater than zero...")
                    continue 

                amount = validing_amount

            except ValueError:
                print("type a valid input")
             
        
        self.balance -= amount
        self.wallet += amount
        print(f"the amount was sucesfully withdran: current balance")
        Bank.show_state(self)
        return 
    
    def deposit(self):
        if self.wallet <=0:
            print("you don't have nothing to desposit...")
            return 


        print("enter your amount to deposit:")

        amount = None
        while amount == None:
            try:
                validing_amount:float=float(input())
                if validing_amount <=0:
                    print("it must be grater than zero...")
                    continue 
                if validing_amount > self.wallet:
                    print("insufecent fonds!!!")
                    continue


                amount = validing_amount
            except ValueError:
                print("enter a valid amount...")

        self.balance += amount
        self.wallet -= amount
        print("your deposit was sucefully deposited")
        Bank.show_state(self)
        return 
        
    def borrow_money(self):
        if self.debt >= 200:
            print("you need to pay your current debt...")
            return 
        
        print("we can only give you $200")

        borrow = None
        while borrow == None:
            try:
                amount=float(input())

                if amount > 200:
                    print("you can't borrow too mucn!!")
                    continue

                if amount <=0:
                    print("it must be greater than zero!!")
                    continue 

                reach_amount=  200 - self.debt + 1

                if amount >= reach_amount:
                    print("that will reach your debt...")
                    continue 

                self.balance += amount
                self.debt += amount
                borrow = amount
                Bank.show_state(self)
                return 

            except ValueError:
                print("Enter a valid input")

    def pay_debt(self):
        if self.debt <= 0:
            print("don't worry, you don't need to pay anything, have a nice day :)")
            return 
        
        print(f"Pay your current debt {self.debt}")
        
        borrow = None
        while borrow == None:
            try:
                amount=float(input())

                if amount > self.balance:
                    print("INSUFECENTS FONDS!!")
                    continue

                if amount <= 0:
                    print("it must be greater than zero!!")
                    continue 

                if amount > self.debt:
                    print("you are going to pay more..., please just pay the right amount")
                    continue 
                   


                self.balance -= amount
                self.debt -= amount
                borrow = amount
                Bank.show_state(self)
                return 

            except ValueError:
                print("Enter a valid input")


#29/08/2025
class Mydict: 
    """
    My class to create dictionaries using two list. To acces the dictionary; use the method 
    Mydict().dict_
    
    """

    def __init__(self,default:Any=None,/) -> None:
   
        self._default:Any=default

        self._dictionary:defaultdict=defaultdict(default)
        
    def __getitem__(self,key)->Any: 
        """Get the value using square brackets"""
        return self._dictionary[key]
    
    def __len__(self)->int: 
        return len(self._dictionary)

    def __iter__(self): 
        return iter(self.dict_)

    def __repr__(self) -> str:
        return f"Mydict(_default={self._default},self._dictionary={self._dictionary})"




    def setvalues(self,keys:list[Hashable],values:list[Any],/)->Self:
        """Here is where you can create the dictionary at hand.
        if there is not enough values for the key provided, it will storage with the default value
        of the class.

        parameters:
            keys: This must be a list of hashables objects, It will be the key of the dict
            values: Second list, this could anything value
        
        """
        
        for key,value in zip_longest(keys,values,fillvalue=self._default): 
            self._dictionary[key] = value 

                 
        print("The values was successully added")
        return self

    def get(self,key:Hashable,/)->Any:
        try:
            return self._dictionary[key]
        except KeyError: 
            return self._default
    
    def keys(self)->list[Hashable]: 
        return [key for key in self.dict_]
    

    def items(self)->list[Tuple[Hashable,Any]]: 
        return [items for items in zip(self.keys(),self.values())]


    def values(self)->list[Any]: 
        return [value for value in self.dict_.values()]

    @property
    def  dict_(self)->dict: 
        """Use this property to get the dictionary"""
        return dict(self._dictionary)
    
    @property
    def defaultvalue(self)->Any: 
        return self._default
    
    @defaultvalue.setter
    def defaultvalue(self,value)->None:
        print(f"The default value '{self._default}' was turn into '{value}'")
        self._default =value

 


        


