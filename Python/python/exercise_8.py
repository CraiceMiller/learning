#grandfather class
class Person:
    school_name = "Shinomiya School S.A."


    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age
        return 
    
    def introduce(self)->None:
        print(f"Hello i am {self.name}, i am  {self.age} years old.")
        return 
    
    def speak(self)->None:
        import random as r
        thing_to_say=["hello","bye","it's late!","i am boring","i'm hungry","let's finished this..."]
        print(f"{self.name} says: {r.choice(thing_to_say)} ")
        return 
    
    def paid(self)->None:
        amount_paid = 0
        if not self.get_paid:
            print(f"you can't get paid...")
            return 
        
        if self.department == "Computer":
            amount_paid = 1700
            print(f"Because of their work, {self.name} receive ${amount_paid} ")
            return 
        
        if self.department == "Art":
            amount_paid = 1500
            print(f"Because of their work, {self.name} receive ${amount_paid} ")
            return 

        
    

    pass

#parents classes:
class Employee(Person):
    def __init__(self, name: str, age: int, employee_id:str,department:str) -> None:
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department 
        return 
    
    def work(self)->None:
        print(f"{self.name} is performing general employee duties in the {self.department} department.")
        return 
    
    def introduce(self) -> None:
         super().introduce()
         print(f"I am an employee at the {Person.school_name}")

    
    pass

class Student(Person):
    class_attribute_year= 2025
    num_students = 0
    def student_adult(age)->bool:
        if  age>= 18:
            return True
        else:
            return False
        
    def __init__(self, name: str, age: int,school_year:int,is_student:bool) -> None:
        super().__init__(name, age)
        self.school_year = school_year
        self.is_student = is_student
        self.get_paid = False
        self.is_adult = Student.student_adult(age)

        self.organized = {"name": name, "age": age,  "Is adult": self.is_adult}

        Student.num_students += 1
        return 
    
    def show_status(self)->None:
        print("-"*15+f"status of {self.name}" + "-"*15 )
        for key,value in self.organized.items():
            print(f"- {key:.<20}{value} ")
    
    

    @classmethod
    def show_num_students(cls)->None:
        print(f"there are {cls.num_students} students here") 
    
    def introduce(self) -> None:
        super().introduce()
        print(f"I am a student at {Person.school_name}, and currently I'm in my {self.school_year}th year, Nice to meet you !")
    
#child classe
class Teacher(Employee):
    def __init__(self, name: str, age: int, employee_id: str,
                  department: str, teaching_specialty:str,years_at_university :int ) -> None:
        super().__init__(name, age, employee_id, department)

        self.teaching_specialty =teaching_specialty 
        self.years_at_university =years_at_university
        self.is_student = False 
        self.get_paid = True
        return 
    
    def teach(self)->None:
        print(f"{self.name} is teaching about {self.teaching_specialty}.")
    
    def work(self) -> None:
        super().work()
        print(f"Due their {self.years_at_university} years at the university, {self.name} can teach {self.teaching_specialty} so well")
        return 
    
    def introduce(self) -> None:
        super().introduce()
        print(f"And I am a teacher, my speciality is {self.teaching_specialty}, Nice to meet you!")


    pass



def main():
    # creating the objects
    teacher_1=Teacher("Sarah",27,"M101-2","Computer",
                    "Computer Scince",6)

    teacher_2=Teacher("Brunet",30,"M101-2","Art",
                    "Character design",4)

    student_1 = Student("Craice",19,3,True)

    #testing the methods
    teacher_1.introduce()
    teacher_1.work()
    teacher_1.speak()
    teacher_1.paid()
    print()

    teacher_2.introduce()
    teacher_2.paid()
    print()

    student_1.introduce()
    student_1.speak()
    student_1.paid()
    print()


if __name__ == '__main__':
    main()