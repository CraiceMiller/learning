import random as r
from datetime import datetime
from iterables_to_use import sentences
from typing import Literal 

"""
DESCRIPTION: 
    In this files you can get the Person class. For now is just a very basic class. 
"""

"""
#0. polymorphism = Greek word that means to "have many forms or faces"

#1. Duck Typing= Another way to achive polymorphism besides Inheritance
#             Object must have the minimum necessary attributes/methods
#             if it looks like a duck and quacks like a duck, it must be a duck

#2. Staticmethod= A method that belongs to a class rather than any objects from that class
#                  It only belongs to the class itself

#3. Classmethod = Allow operation related to the class itself
                # take (cls) as the first parameter, wicht is the class itself

#4. Instance methods

#5. Dunder methods = They are automatically called by many of python's built-in operators.
#                     They allow developers to define or customize the behavior of objects

#6. dataclass

"""


"""
HOW TO WRITE BETTER FUNTIONS (by indently.io_):
    1. Write short and concise 
        Examples:
        - get_number
        - display_number
    
    2. Specify a return type 
        Example:
        -> None
        -> str
        -> int

    3. Make as simple and reusable as possible 
        Example:
        A function that only do one single task

    4. Document all your functions: 
        Example: 
        Write the core purpose of the funtion, what it does, what paremeter takes
        what it returns, an example.
        >>> get_number()
            output: 2

    5. Handles the errors appropriately:
        Example:
        raise ValueError
        raise TypeError
    

"""

#update: 5/8/25: type annotations



class Person:
    """
    Description: 
        This is a bluprint of a basic clasic person and does simple things like speak or sleep
        here you can add variable like names, likes, belief, so on. 
        well, this is pretty much it
        here I will attempt to code everything i will learn

    Return:
        a Person class 

    Update:
        30/07/2025
    """
    #Class funtions
 
    def get_hour(self)->int:
        """
        DESCRIPTION: 
            This method only get the hour if 24 hours format
            from the local time...

        RETURN: 
            An strings

        EXAMPLE:
            >>> get_hour()
                output: '5'
        """

        now=datetime.now()
        return int(now.strftime("%H"))
    
    def get_time_str(self)->str:
        """
        DESCRIPTION: 
            This method get anohter method get_hour(), and based on that
            will return a massage accordenly of the current hour. 
            -morning: 5:00 - 12:00
            -afternoon:12:00 -17:00
            -evening:17:00 - 21:00
            -night: 21:00 - 5:00
                    
        RETURN: 
            the text as a sting

        EXAMPLE:
            >>> get_time_str()
                output: 'evening'
        """
        text:str=""

        #get the main greet
        if self.get_hour()>= 21 or  self.get_hour() < 5:
            text="night"
        elif self.get_hour()>=17:
            text="evening"
        elif self.get_hour()>=12:
            text="afternon"
        elif self.get_hour()>=5:
            text="morning"

        return text
   
    def get_status(self)->str:
        """
        DESCRIPTION: 
            This method will track the current tired rate of the peson at hand,
            and return a text based of that (eg. if the person tired rate is 60, 
            it will display 'has energy'). This method is created of if/elif statements


        RETURN: 
            A text as a string 

        EXAMPLE:
            >>> get_status()
                output: "getting tired"
        """
        if self._tired_rate > 95:
            return "full"
        elif self._tired_rate > 50:
            return "has energy"
        elif self._tired_rate >30:
            return "ok"
        elif self._tired_rate >20:
            return "getting tired"
        elif self._tired_rate > 0: 
            return "tired"

        return "exhausted"
    
    #class varibles
    text_negative:str="Can't do this action"



    #defining dunderscore methods
    def __init__(self,
                name:str,
                lastname:str,
                age:int,
                language:list,
                
                gender:Literal["male","female"]="male",
                profession:str='student',
                birthaday:str|None=None,
                height:float|None=None,
                weight:float|None=None,
                country:str|None=None,
                temperament:str|None=None,
                likes:list[str] |None=None,
                dislikes:list[str]|None=None,
                weaknesses:list[str]|None=None,
                strenghts:list[str]|None=None,
                beliefs:list[str]|None=None,
                fears:list[str]|None=None
                ) -> None:
        """
        DESCRIPTION: 
            This method will storage basic iformation of the person. 

        PARAMETERS:
            name: Write the name of the person
            lastname: write the name of the person 
            age: this must be an integer, and this will storage the age of the person 
            langugue: this parameter is obligatory to dicide wich language this person can speak
            gender: this only can be wheather a male or female
            profession: if the person has a job or any special profession, student otherwise

            The others parameters are optionals, if you only want to give it more info about 
            the character


        RETURN: 
            A Person object

        EXAMPLE:
            >>> Person("Hersy","Halston",18,["spanish"],"male")
                output: Person
        """
        #info given
        self._name = name
        self._age = age
        self._lastname=lastname
        self._gender=gender
        self._language=language
        self._profession=profession
        self._birthday=birthaday
        self._height=height
        self._weight=weight
        self._country=country
        self._temperament=temperament
        self._likes=likes
        self._dislikes=dislikes
        self._weaknesses=weaknesses
        self._strengths=strenghts
        self._beliefs=beliefs
        self._fears=fears
        #extra info
        self._is_sleeping:bool=False
        self._tired_rate:int=100
        self._has_hungry:bool=False
        self._doing_action:bool=False
        
    
    def __str__(self) -> str:
        return f"Person: {self._name}"
    
    def __eq__(self, __value) -> bool:
        return self._name == __value._name and self._lastname == __value._lastname and self._age == __value._age
    
    def __format__(self, __format_spec: str) -> str:
        if __format_spec == 'show':
            return f"{self._name} {self._lastname}, {self._age} years old, {self._gender}"
        if __format_spec == "status":
            return f"Currently status of {self._name }: {self.get_status()}"
        return 'N/A'
    
    def __getitem__(self,key:str):
        if key == 'name':
            return f'{self._name}'
        

    #Methods
        
    
    def introduce(self)->None:
        """
        DESCRIPTION: 
            This method only display in the terminal a little introduce of 
            the currently characater (Person object)

        RETURN: 
            None

        EXAMPLE:
            >>> introduce()
                output: My name is Hersy, I am 18 years old. Nice to meet you 
        """
        
        print(f"My name is {self._name}, I am {self._age} years old. Nice to meet you ")

    def greet(self, _otherperson=None)->str:
        current_hour:int=self.get_hour()
        text:str=self.get_time_str()

        if _otherperson is not None:
            print(f"Good {text.capitalize()} {_otherperson._name}!!!")
        else:
            print(f"Good {text.capitalize()}")
    
        return text

    def speak(self)->None:
        
        thing_to_say:tuple=sentences
        print(f"{self._name} says: {r.choice(thing_to_say)} ")
       
    def sleep(self)->None:
        current_hour = self.get_hour()

        if  self._is_sleeping:
             print(f"{self._name} is sleeping, shh!!, {self.text_negative}")
             return
        
        if (current_hour >= 21 or current_hour < 5): 
            print(f"It's too late,therefore  {self._name} starts to sleep")
            self._is_sleeping=True
            self._doing_action=False
            return 
     
         
        
        if not (current_hour >= 21 or current_hour < 5): 
            print(f"{self._name} cannot sleep right now (it's {current_hour}:00, not sleeping hours).")
            return
        
        if self._tired_rate > 25: 
            print(f"{self._name} is not tired enough to sleep (tiredness: {self._tired_rate}%).")
            return
        
        
        
        print(f"{self._name} starts to sleep")
        self._is_sleeping=True
        self._doing_action=False
    
    def wake_up(self,urgency:bool=False)->None:
        if not self._is_sleeping:
            print(f"This person is already wake,{self.text_negative}")
            return 
        
        if urgency:
            currently:int=self._tired_rate
            self._tired_rate= int(currently + ( currently * 0.05))
            self._is_sleeping=False 
            print(f"{self._name} asks: What's happend?")
            return 

        
        current_hour = self.get_hour()
        if (current_hour >= 21 or current_hour < 5): 
            print(f" {self._name} needs to sleep, so please don't bother them")
            return 
        
        print(f"{self._name} wakes up")
        self._is_sleeping=False
        self._tired_rate=100
        print(f'{self:status}')
        


    def walk(self)->None:
        if self._is_sleeping:
            print(f"{self._name} is sleeping, {self.text_negative}")
            return 
        
        print(f"{self._name} is walking")
        self._tired_rate -= 3
            


if __name__ =="__main__":
    person1:Person=Person("Craice","Miler",18,["spanish"],"female",) 
    person2:Person=Person(
                          "Hersy","Halston",18,["spanish"],"male","student",
                          'April 12th',70.50,135.50,'Altisora','sanguine-choleric',
                        ['play videogames', 'exercising', 'hang out with friends',
                         'animes', 'living', 'watch animes, series, doramas, movies, novels',
                        'female fashion', 'ethical classes', 'make up'],
                        ['spicy & salty food', 'feling lonely', 'bad habbits'],
                        ['overcompensation', 'difficulty handing loneliness', 'problem avoidance'],
                        ['intiative', 'fun-loving', 'bold', 'not too fluent in a foreign language', 'leadership' ],
                        ['god', 'health', 'her family & friends', 'education', 'himself'],
                        ['clowns']) 
 

    person2.introduce()
    person2.greet(person1)
    person2.speak()
    person2.sleep()
    person2.wake_up()
    print(person2.get_hour())
    person2.sleep()
    print(person2._tired_rate)
    person2.sleep()
    print(f"{person2:show}")
    person2.walk()
    person2.wake_up(True)
    person2.walk()
    print(f"{person2:status}")
    print(person2._tired_rate)
    person2.sleep()
    person2.walk()
    person2.wake_up()
    person2.speak()


