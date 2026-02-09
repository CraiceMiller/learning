from time import sleep
import random

class Robot:
    user= "sthephany Whelthon"
    def __init__(self, name) -> None:
        self.name=name
        self.is_sleep= True
        self.is_running = False
        self.is_tired = False
        self.turn_on= False
       

    def greet(self):
        if   self.is_sleep:
            print(f"{self.name} is currently sleeping")
            return 


        print(f"Greeting {Robot.user.capitalize()}, I am {self.name} and i will be your personal assintence")
        return 

    def run(self):
        if   self.is_sleep:
            print(f"{self.name} is sleeping, shh!!")
            return
        
        self.is_running = True
        print(f"{self.name} starts to run...")

    def stop_run(self):
        if   self.is_sleep:
            print(f"{self.name} is sleeping, shh!!")
            return
         
        if self.is_running:
            self.is_tired = True
            self.is_running= False
            print(f"{self.name} stops to run, now it is tired")
            return 
        
        print(f'{self.name} was not running...')


    def sleep_robot(self):
        if  self.is_tired:
            print(f"{self.name} can't sleep, cuz it is tired, drink something....")
            return 
        
        if self.is_running:
            print(f"{self.name} can't sleep cuz, it is running...")
            return 

       
        self.is_sleep=True
        print(f"good night {Robot.user.capitalize()},{self.name} appriciete helps you...")
        print(f"{self.name}'s sleeping now...!, ")
        print("\n")

    def drink(self):
        if   self.is_sleep:
            print(f"{self.name} is sleeping, shh!!")
            return
        
        if self.is_running:
            print(f"{self.name} it can 't drink cuz it is running..")
            return 
        
        if self.is_tired:
            self.is_tired = False
            print(f"{self.name} starts to drink a bottle of watter...")
            return 
        
        
        print(f"{self.name} is not tired")

    def turn_on_robot(self):
        if  not self.is_sleep:
            print(f"{self.name} is already turn on!!")
            return 


        self.turn_on= True
        self.is_sleep= False

        print("turning on, please hold on")
        for i in range(3):
            print(".")
            sleep(1)

        print(f"{self.name} is now turn on, now it can do anything you want... ")
        Robot.greet(self)
        print("\n")
        return 
        
        

    def recomend_something(self):
            if   self.is_sleep:
                print(f"{self.name} is sleeping, shh!!")
                return
            
            if   self.is_running:
                print(f"{self.name} is running, can't answer you")
                return
            
            if   self.is_tired:
                print(f"{self.name} is tired, can't answer you")
                return
            
        


            stuff = ["check your bills" ,"do exercise", "go out with your friends", "take a bath", "watch a movie", "work", "keep coding"]
            choose_robot = None

            while choose_robot == None:
                choose_robot= random.choice(stuff)

            if choose_robot == "take a bath":
                print(f"{self.name} can recomends you to {choose_robot}, you reeks... ")
                return
            
            if choose_robot == "keep coding":
                print(f"{self.name} can recomends you to {choose_robot} ")
                print("YOU ARE DOING GREAT SO FAR!!! ")
                return
            


            print(f"{self.name} can recomends you to {choose_robot} ")
        
       
   

        
print("-----my attempt-----")
R_23=Robot("R_23")

R_23.turn_on_robot()
print()
R_23.recomend_something()
R_23.recomend_something()

R_23.run()
R_23.stop_run()
R_23.drink()
R_23.sleep_robot()


help(help)










    



    

