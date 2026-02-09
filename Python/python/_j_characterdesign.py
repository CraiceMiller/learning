from random import randint,choice
#grandfather class
class Caracher:
    def __init__(self,name:str) -> None:
        self.name = name

    def attack(self, target):
        print(f"{self.name} attacks {target.name} ")
        return 
    
    def show_status(self):
        characters_info = {"name": self.name,
        "power attack": self.pw_attack,
      "maggia": self.mg_attack,
       "gold": round(self.gold,2),
      "health": round(self.health,2)}
        
        print("-"*15+"CHARACTER INFO"+"-"*15)
        for key,value in characters_info.items():
            print(f"{key.capitalize():.<15}:{value}")

    def simple_attack(self,target):
        attacking = self.pw_attack * 0.45
        target.health -= attacking 
        print(f"{self.name} attacks {target.name}")
        print(f"{target.name} recieve {attacking} of damange")
        print(f"{target.name}'health: {target.health}")
        

#super class or father classes
class Villians(Caracher):
    
    def __init__(self, name: str,) -> None:
        super().__init__(name)
        self.is_evil = True

    def thief(self,target):
        
        amount_stealing = randint(0,target.gold)
        target.gold -= amount_stealing
        print(f"{self.name} steal G{amount_stealing} from {target.name}")
        return 


class Heroes(Caracher):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.is_evil = False

    def courage(self):
        old_pw = self.pw_attack
        self.pw_attack = self.pw_attack+(self.pw_attack * 0.55)
        print(f"{self.name} feel the power to keep fighting to the sake of everyone")
        print(f"their power attack increase: before {old_pw}/now:{self.pw_attack}")


#child clases or subclases
class Knight(Heroes):
    default_health = 1200
    def __init__(self, name: str,gold:int=300) -> None:
        super().__init__(name)
        self.pw_attack= 195
        self.mg_attack= 5
        self.gold=gold
        self.health=Knight.default_health

class Wizard(Heroes):
    default_health = 1000
    def __init__(self, name: str,gold:int=250,health:int=default_health) -> None:
        super().__init__(name)
        self.pw_attack= 15
        self.mg_attack= 150
        self.gold=gold
        self.health= health

    #supposedly this are the uniques attacks from the wizard class
    def explosion(self,target):
        attacking = self.mg_attack+(self.mg_attack * 0.95)
        target.health -= attacking
        self.health -= (attacking * 0.25)

        print(f"{self.name} says:EXPLOTIOOONNNSSS...!!!")
        print(f"{target.name} took {attacking} of damange")

class Gobling(Villians):
    default_health = 800
    def __init__(self, name: str,gold:int=0,health:int=default_health) -> None:
        super().__init__(name)
        self.pw_attack= 85
        self.mg_attack= 45
        self.gold=gold
        self.health= health

class Mercenary(Heroes,Villians):
    default_health = 1000
    def __init__(self, name: str,gold:int=550,health:int=default_health) -> None:
        super().__init__(name)
        self.pw_attack= 105
        self.mg_attack= 45
        self.gold=gold
        self.health= health

#sub-sub classes i think
class IceWizard(Wizard):
    def __init__(self, name: str, gold: int = 250) -> None:
        super().__init__(name, gold)

    def blizzard(self,target):
        attacking = self.mg_attack * 0.45
        target.health -= attacking

        print(f"{self.name} use blizzar with {target.name}")
        print(f"{target.name} took {attacking} of damange!")


class DarkWizard(Wizard):
    def __init__(self, name: str, gold: int = 250, health: int = Wizard.default_health) -> None:
        super().__init__(name, gold, health)
        self.dk_attack = 170
        

    def dark_ball(self,target):
        attacking = self.dk_attack * 0.55
        target.health -= attacking

        print(f"{self.name} use dark ball with {target.name}")
        print(f"{target.name} took {attacking} of damange!")
        return 
    

#sub sub sub class
class MegaDarkWizard(DarkWizard,Villians):
    def __init__(self, name: str, gold: int = 250, health: int = Wizard.default_health) -> None:
        super().__init__(name, gold, health)
      

    def destroy(self,targets:set[Caracher]):
        attacking = self.mg_attack * 10
        self.health = 0

        print(f"{self.name} destroy themself and damge everyone in the field...")
        # for every person in the field the attack will subside...
        for target in targets:
            if target is not self:
                        target.health -= attacking
                        print(f"{target.name} took {attacking}")

                        attacking -= 150

            

        


#creating objects...
knight=Knight('Arthur')
wizard=Wizard("Megumin")
gobling=Gobling("gobling")
ice_wizard=IceWizard("Kazumi")
dark_wizard=DarkWizard("Sahara",2000,1200)
mega_dark_wizard = MegaDarkWizard("Drokander",health=2000)
mercenary=Mercenary("Belthon")

#crating a list 
all_characters=[knight,wizard,gobling,ice_wizard,mega_dark_wizard,dark_wizard,mercenary]

#showing all the status 
for status in all_characters:
    status.show_status()
    print()

#testing methos 

selection_character = choice(all_characters)
gobling.thief(selection_character)

selection_character = choice(all_characters)
wizard.explosion(selection_character)

selection_character = choice(all_characters)
dark_wizard.dark_ball(selection_character)

selection_character = choice(all_characters)
mega_dark_wizard.thief(selection_character)

selection_character = choice(all_characters)
knight.simple_attack(selection_character)

selection_character = choice(all_characters)
mercenary.simple_attack(selection_character)

selection_character = choice(all_characters)
dark_wizard.simple_attack(selection_character)



knight.courage()
knight.simple_attack(mega_dark_wizard)

#see the alive people
alive_characters=[char.name for char in all_characters if char.health > 0]
print(alive_characters)


print()
#
targets=set(all_characters)
mega_dark_wizard.destroy(targets)


#see the alive people but in another way
alive_characters = []
dead_characters = []
for character in all_characters:
    if character.health <= 0:
        print(f"{character.name} has dead..")
        dead_characters.append(character)
        continue

    else:
        print(f"Name: {character.name}, Health {character.health}")
        alive_characters.append(character)

if alive_characters == []:
    print(f"every charcter has dead")
else:
    print("characters reamains...")
    num = 1
    for i in alive_characters:
        print(f"{num}. {i.name}")
        num += 1

print()
if not dead_characters == []:
    print("characters dead...")
    num = 1
    for i in dead_characters:
        print(f"{num}. {i.name}")
        num += 1
else:
    print("No ones have dead...")

if not alive_characters == [] and not dead_characters == []:
    print(f"{choice(alive_characters).name} feels sad for {choice(dead_characters).name}'s death...")


#  fours hours straight... :|