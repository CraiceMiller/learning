#superclass or Father classes
class Animal:
    def __init__(self, name:str,has_claws:bool) -> None:
        self.name = name
        self.has_claws = has_claws
        return 
    
    def eat(self)->None:
        print(f"{self.name} is eating")
        return 
    
    def sleep(self)->None:
        print(f"{self.name} is sleeping...")
        return 
    
    def describe(self)->None:
        print(f"name: {self.name}. Has claes {self.has_claws}")


class Prey(Animal):
    def flee(self)->None:
        print(f"{self.name} is fleeing...")
        return 

class Predator(Animal):
    def hunt(self)->None:
        print(f"{self.name} is hunting...")
        return 
    
    def cut(self):
        if self.has_claws:
            print(f"{self.name} is cutting")
            return 
        else:
            print(f"{self.name} can't cut")
    

# Subclasses or Children classes
class Rabbit(Prey):
    def __init__(self, name: str, has_claws: bool) -> None:
        super().__init__(name, has_claws)

    def dig(self)->None:
        print(f"{self.name} is digging... ")

class Bear(Predator):
    def __init__(self, name: str, has_claws: bool,high:float) -> None:
        super().__init__(name, has_claws)
        self.high = high

    def describe(self) -> None:
        super().describe()
        print(f"high: {self.high}")


    def climb(self)->None:
        print(f"{self.name} is climbing...")

class Fish(Prey, Predator):
    def swim(self):
        print(f"{self.name} is swimming...")
        return 
    def describe(self) -> None:
        super().describe()
        print("indeed it is a fish...")
        return 




#crating the objects...
rabbit = Rabbit("Rabbit",False)
fish = Fish("fish",False)
bear = Bear("Bear",True,78.50)

#testing their behaviors...
rabbit.flee()
rabbit.eat()
fish.hunt()
bear.cut()
fish.cut()
rabbit.describe()
bear.describe()
fish.describe()




