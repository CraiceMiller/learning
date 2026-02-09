#5/8/25
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

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import ClassVar
from random import shuffle

class Animal:
    alive:bool=True

    @staticmethod
    def is_animal(animal:object)->bool:

        if not isinstance(animal,(Duck, Wolf)):
            return False

        return True
    
    @classmethod
    def is_alive(cls)->bool:
        return Animal.alive

class Duck(Animal):
    def speak(self)->None:
        print("CUACK!! ")


class Wolf(Animal):
    def speak(self)->None:
        print("WOOF!!")

class Car:
    alive:bool=False

    def speak(self)->None:
        print("HONK!!")

def main()->None:
    #Duck typing
    duck=Duck()
    wolf=Wolf()
    car=Car()

    animals:list=[duck, wolf, car]

    for animal in animals:
        animal.speak()
        print(animal.alive)

    for valid in animals:
        print("It is an animal" if Animal.is_animal(valid) else "No, it is not  an animal")
    print()
    for _ in animals:
        print("It is alive" if Animal.is_alive() else "No, it is not  a alive")

    print()

@dataclass(slots=True,order=True)
class Person(ABC):
    _name:str

    _is_alive:bool=field(init=False, default=True)

    count_people:ClassVar=0


    def __str__(self) -> str:
        return f"Name: {self._name.capitalize()}"
    
    def __eq__(self, __value) -> bool:
        return self._name == __value._name
    
    def __post_init__(self)->None:
        Person.count_people +=1 
    
   

    @abstractmethod
    def type_person(self):
        pass

    def greet(self)->str:
        return "Hello I am a person. "
    



class Employee(Person):
    count:int=0

    def __init__(self,
                 name: str,
                 position:str,) -> None:
        super().__init__(name)
        self._position=position

        Employee.count += 1
    
 




    def type_person(self)->str:
        return "employee"


    def get_info(self)->str:
        return f"{self._name.capitalize()} | {self._position:<10} "
    
    def greet(self) -> str:
        return super().greet() + "MY name is {}, and my position is {}. ".format(self._name,self._position)
    
    @staticmethod
    def is_valid_positon(job_position)->bool:
        valid_positions:list=['manager','cashier','cook','janitor']
        return job_position.lower() in valid_positions
    
    @classmethod
    def count_employees(cls)->int:
        return Employee.count


class Student(Person):
    count:int=0
 

    def __init__(self,
                 name:str,
                 grade:str,
                 ) -> None:
         super().__init__(name)
         self._grade=grade
        

         Student.count += 1


    def type_person(self)->str:
        return "student"


    def get_info(self)->str:
        return f"{self._name.capitalize()} | {self._grade:<20} "
    
    def greet(self) -> str:
        return super().greet() + "MY name is {}, and I'm studying  {}. ".format(self._name,self._grade)
    
    @staticmethod
    def is_valid_career(career)->bool:
        valid_careers:list=['management','bachelor','accountant']
        return career.lower() in valid_careers
    
    @classmethod
    def count_students(cls)->int:
        return Student.count

class Furry(Student,Animal):
 

    def __init__(self, name: str, grade: str,kind:str) -> None:
        super().__init__(name, grade)
        self._kind=kind
        
 
    def type_person(self)->str:
        return "student"


    def get_info(self)->str:
        return f"{self._name.capitalize()} | {self._grade:<20} | {self._kind:<20} "
    
    def greet(self) -> str:
        return super().greet() + "and I am a {}".format(self._kind)
    





def main2()->None:
    #Employees
    employee1=Employee("Sergio",'Manager')
    nw_employee=Employee("stephany","cook")
    person=Employee("hersy","student")
    employees=[employee1, nw_employee, person]
    for info in employees:
        print(info.get_info())

    print()

    for valid in employees:
        print("It is a valid Job" if Employee.is_valid_positon(valid._position) else "No, it is not a job")

    print("Num. of employees: {}".format(Employee.count_employees()))

    for person in employees:
        print(person.greet())

    #Students
    student1=Student("Edward",'management')
    nw_student=Student("cristy","singer")
    person2=Student("ashley","bachelor")
    students=[student1, nw_student, person2]

    for information in students:
        print(information.get_info())

    print()

    for validing in students:
        print("It is a valid career" if Student.is_valid_career(validing._grade) else "No, it is not a career")

    print("Num. of Students: {}".format(Student.count_students()))

    for p in students:
        print(p.greet())

    print()




    #Students
    student2=Furry("Pardo",'management','bear')
    student3=Furry("tamaki","bachelor",'squid')
    furry=Furry("juanjo","bachelor",'cat')
    furry_students=[student2, student3, furry]

    for information in furry_students:
        print(information.get_info())

    print()

    for validing in furry_students:
        print("It is a valid career" if Student.is_valid_career(validing._grade) else "No, it is not a career")

    print("Num. of Students: {}".format(Student.count_students()))

    for p in furry_students:
        print(p.greet())

    print()
    for fur in furry_students:
        print("It is alive" if fur.is_alive() else "No, it is not  a alive")
    

        


    #classes
    print()
    all_objects:list=[]
    all_objects.extend(employees)
    all_objects.extend(students)
    all_objects.extend(furry_students)
    shuffle(all_objects)

    for obj in all_objects:
        if obj.type_person() == "employee":
            print(f"{obj._name} is an employee")
            continue
        if obj.type_person() == "student":
            print(f"{obj._name} is a student")
    
    var=all_objects[0]
    for i in all_objects:
        print(i)
        print(i==var)

    print()
    print(f"NO. of person here {Person.count_people}")
      
            






if __name__ == '__main__':
    main()
    main2()