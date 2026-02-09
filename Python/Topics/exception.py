#16/08/2025
class MyExceptions: 

    def greet(self,name,age:str)->None: 
        try: 
            print(f"Hello {name}, You are {int(age)}")
        except ValueError as e:
            print(f"{name} you need to type a number. {e}")
        finally: 
            print("Bye")

    def divison(self, num:str,num2:str)->float|str:
        try: 
            return float(num) / float(num2)
        except ValueError as e: 
            return f"{e}"
        except ZeroDivisionError as e:
            return f"{e}"
        
value=MyExceptions()
value.greet("hello","hersy")
print(value.divison("10","hello"))
print(value.divison("10","0"))
print(value.divison("10","2"))
value.greet("hello","19")
