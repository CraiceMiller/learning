#Inheritance = Allows a class inherit attribures and methods from another class
#              Helps with code reusability and extensibily#
#              class Child(Parent)

class Animal:
    def __init__(self,name:str) -> None:
        self.name = name
        self.is_alive = True
        return 
    
    def eat(self)->None:
        print(f"{self.name} is eating...")
        return
    
    def sleep (self)->None:
        print(f"{self.name} is sleeping..")
        return 
    
class Duck(Animal):
    def speak(self):
        print(f"{self.name} says: QUACK!,QUACK!")

class Rakkun(Animal):
    def __init__(self,name:str,country:str):
        super(name)
        self.country = country
    
    def speak(self):
        print(f"Country: {self.country} ")
        print(f"{self.name} says: Coo!, Coo!")


duck = Duck("Pato")
rakkun = Rakkun("Raptalia")
duck.sleep()
duck.speak()
rakkun.speak()