#1. firt we have the class statement....
class Friends:
    #2.class attributes = works the same as a varible but only insde a class statement
    num_of_friends:int= 0
    count= 4
    
    # 3. The Constructor Method (Initializer)
    def __init__(self, name:str, age:int,  hight:float, student:bool, mood:str="happy" )->None:
        # 3.1 Instance Attributes (unique to each object)
        self.self=self
        self.a = name
        self.age = age
        self.hight = hight
        self.student = student
        self.mood= mood
        print(f"a new person has been added, they name is {name.capitalize()}")
        Friends.num_of_friends +=1

    # 4. Instance Methods
    def go_school(self)->None:
         if self.student:
              print(f"{self.a} is time to study for the exam!! ")
         else:
              print(f"{self.a} is time to attached the worksheets to your boos!!")
    
    def get_happy(self)->None:
         self.mood="happy"
         print(f"{self.a} is now happy !!!")

    def get_student(self)->None:
         if not self.student:
              self.student=True
              print(f"{self.a} is a student now, you can go to school")
         else:
              print(f"{self.a} is already a student ")

    
    def state(self)->None:
         if self.mood != "happy":
              print(f"{self.a} is sad right now...")
         else:
              print(f'{self.a} is happy !!')

    def phrase(self):
         while not self.age <= 0:
              print("everything is gonna be okay")
              self.age -= 5

    def phrase_2(self):
         while not Friends.count <= 0:
              print("you\'re doing great, not give up now!!")
              Friends.count -=1
         

        
        

    # 5. Class methods
    @classmethod
    def get_count(cls)->str:
            return f"total of friends: {cls.num_of_friends} "

    @classmethod 
    def parameters(cls):
         ...
         



    



people="craice" #2.1 this is a variable....

def person(name:str, age:int,  hight:float, student:bool): # 3.2 it is the same 
    pass


p1=Friends("hesy", 18,68.5,True)
p2=Friends("craice", 19,65.2,False,"sad" )
print(people)
print(Friends.num_of_friends)
print(__name__)
print(p1.a)
print(Friends.get_count())
p1.go_school()
p2.go_school()
p1.get_student()

print("-----------")
print(f"this person is called {p2.a}")
p2.state()
p2.go_school()
p2.get_happy()
p2.state()
p2.get_student()
p2.go_school()
p2.phrase()
p2.phrase_2()




