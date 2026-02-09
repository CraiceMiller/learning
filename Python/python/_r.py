import random as r 
from datetime import datetime
from operator import itemgetter
def mini_calulator(*args, symbol)->float|int|None:

    num1:itemgetter=itemgetter(0)
    num2:itemgetter=itemgetter(-1)
    total:float|int=0
    if (symbol=="+"):
        total=sum(args)
    elif(symbol=="-"):
        total=num1(args) - num2(args)
    elif (symbol=="*"):
        total=num1(args) * num2(args)
    elif (symbol=="/"):
        try:
            total=num1(args) / num2(args)
        except ZeroDivisionError:
            return None
    else:
        return None
    return total
        
class PersonalityPersonalAssistance:
    """This are class variable for the class"""

    import random as r 
    from datetime import datetime

    ASSISTANCE_NAME:str = 'ChatBot'
    ASSISTANCE_LIKES:list=['help','sleep','do things', 'write']
    random_sentences:tuple = (
    "The ancient map hinted at a forgotten treasure.",
    "Butterflies fluttered gracefully in the sunlit meadow.",
    "A lone wolf howled at the full moon.",
    "The old clock chimed precisely at midnight.",
    "She dreamt of flying among the stars.",
    "Rain pattered softly on the windowpane.",
    "He found an unusual seashell on the beach.",
    "The city lights twinkled like scattered diamonds.",
    "A curious cat explored the dusty attic.",
    "The aroma of fresh bread filled the kitchen."
)

    @classmethod
    def presentation(cls)->None:
        """This class method only say hello!"""
        print(f"\nHello I'm {cls.ASSISTANCE_NAME}")

    @classmethod
    def speak(cls):
        print(f"{cls.ASSISTANCE_NAME} says: {r.choice(cls.random_sentences)}")

    def give_hour(cls):
        print(f"\nToday is {datetime.now()}")

class PersonalAssistance(PersonalityPersonalAssistance):
    Time_user_call:int=0
    def __init__(self) -> None:
        """This only storage the user info """
        self.user_name:str = "".capitalize()
        self.result_number:float=0.0
        self.user_likes:list=[]
        self.user_age:int=0
        self.user_is_student:bool=None
        PersonalAssistance.Time_user_call += 1
        

    def is_student(self):
        "This only give tell if the user is student or not"
        chosse=input(f'{self.user_name}, are you and student?: ').strip().lower()
        if (chosse!='yes'):
            self.user_is_student=False
        else:
            self.user_is_student=True
            
    def user_mini_calculator(self)->None:
        try:
            num1:float=float(input('Type a number: '))
            symbol:int=input("Type an operator: ")
            num2:float=float(input('Type a number: '))
            result:float|None=mini_calulator(num1,num2,symbol=symbol)
            if (result==None):
                print("An error occur in your calculation")
            else:
                print(f"Your result is {result}")
        except ValueError as e:
            print(f"An error occured not in the calculator: {e}")
    

    def sum_up(self)->None:
        """This print a list of the instances """
        real_things:filter=filter(lambda thing: not thing.isdigit(),self.user_likes)
        new_user_likes:list=list(map(lambda like:like.capitalize(), real_things))

    
        print("-"*40)
        print(f"\nok, this is everything i got so far")
        print(f"Your name is: {self.user_name}")
        print(f"You are {self.user_age} years old")
        print("You're an adult!" if self.user_age >= 18 else "You're still young!")
        print("You're are a student" if self.user_is_student else "You aren't a student")
        print(f"Your sum is: {self.result_number}")
        print(f"Your like: {" and ".join(new_user_likes)}")
        
        print("-"*40)
        
     
    def user_get_name(self)->None:
        """This instance method only say hello to the user"""
        self.user_name:str=input('Hello there! what your name: ')
        print(f"Nice to meet {self.user_name}!, let's be friends :) ")

    def user_sum(self)->None:
        """This only sum two nubers"""
        print(f"ok {self.user_name} let's sum two numbers,shall we?:")
        while(1):
            try:
                number_1:float=float(input('Type the first number: '))
                number_2:float=float(input('Type the second number: '))
                result:float=number_1+number_2
                self.result_number = result 
                print(F"Ok the result is {result:.2f}")
                print('Great Job')
                break;
            except ValueError:
                print(f"{self.user_name} select a valid input please!")

    def user_favorite_thing(self)->None:
        thing:str=""
        print(f"\n What are your favorite things?: ")
        while (1):
            thing:str=input('write it here [write q to quite]').lower().strip()
            if (thing!="q"):
                self.user_likes.append(thing)
                continue 
            break
      
    def user_get_age(self)->None:
        """This only ask the user age"""
        age:int=""
        while not (age.isdigit()):
            age:int=input('How old are you: ')
        self.user_age=int(age)
    
    @classmethod
    def times_user(cls):
        print(f"{cls.ASSISTANCE_NAME} helps {cls.Time_user_call} today!")

def main():
    assistance:PersonalAssistance=PersonalAssistance()

    assistance.speak()
    assistance.give_hour()
    assistance.user_get_name()
    assistance.user_get_age()
    assistance.is_student()
    assistance.user_favorite_thing()
    assistance.user_sum()
    assistance.user_mini_calculator()

    assistance.sum_up()
    assistance2:PersonalAssistance=PersonalAssistance()
    assistance2.speak()
    assistance.times_user()
    
if __name__ == '__main__':
    main()
