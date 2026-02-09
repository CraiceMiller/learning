import random as r
import time as t

class Game: 
    postion = 15
    quantity_positions = 3
    def __init__(self, name:str, health:int=100, skill_1:str="none", skill_2:str="none", attack_min_1:int=30, attack_max_1:int=50,attack_min_2:int=30, attack_max_2:int=60)->None:
        self.name=name
        self.health=health
        self.skill_1=skill_1
        self.skill_2=skill_2
        self.attack_min_1 = attack_min_1
        self.attack_max_1 = attack_max_1
        self.attack_min_2 = attack_min_2
        self.attack_max_1 = attack_max_1
      



    def show_status(self)->None:
        print(f"name: {self.name}, health {self.health}")

    def take_damage(self,damange:float,skill)->None:
        if damange > 0:
            self.health -= damange
            if self.health <0:
                self.health = 0
            print(f"{self.name} took {damange} damange")
            if self.health == 0:
                print(f"{self.name} has been defeated")


    def give_attack(self, target,skill)->None:
        skill= self.skill
        if skill_2=="blade"
        
        actual_attack= r.randint(self.attack_min,self.attack_max)
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(actual_attack)

    

    def heal(self, amount)->None:
        if self.health >0:
            self.helth += amount
            print(f"{self.name} have been heal by {amount}")
        else:
            print(f"{self.name} is default already...")
        




# make three difernte charactes
#make the user chose the chracter to fight
# make the character can do two kind of attack
#make the dragon attacks one random character
# make the character can also drink posion just the avaliables ones
# when a character is defeated the user can't user anymore
# every character can dogde the attack...


c1 = Game(name="Heroe",health=150,skill_1="rapier", skill_2="Blade",attack_min_1=30,attack_max_1=41, attack_min_2=50, attack_max_2=61)

c2 = Game(name="Mage",health=150,skill_1="Fire boll", skill_2="gremory",attack_min_1=34,attack_max_1=43, attack_min_2=40, attack_max_2=70)

dragon= Game("Dragon")
print("----Start the game------")


characters=["Heroe", "Mage"]
while c1.health > 0 and dragon.health > 0:
    print("make your chosse....")
    chosse = input().lstrip().capitalize()
    while chosse not in characters:
        print("choose a valid character...")
        chosse = input().lstrip().capitalize()

    if chosse == "Heroe":
        c1.give_attack(dragon)
        c1.show_status()
        print()

    if chosse == "Mage":
        c2.give_attack(dragon)
        c2.show_status()
        print()


    if dragon.health <= 0:
        break
    t.sleep(1)

    dragon.give_attack(c1)
    dragon.show_status()
    print()

    if c1.health and c2.health <= 0:
        break
    t.sleep(1)

    
print()
if c1.health <= 0:
    print("you lost")
else:
    print("you win!!")




