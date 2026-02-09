#11/07/2025
from math import sqrt
from classes_to_use import *
from functions_to_use import *
from colorama import Fore, Style
from My_Classes import person as p

numbers=-64,-81,-16,-25,-36


square_roots_2 = map(lambda x: sqrt(abs(x)), filter(lambda x:x % 2 == 0, numbers))
print(Fore.YELLOW , list(square_roots_2))

my_items = 'hersy ', 20, 20.52, 'craice', True, 2j, 'ashley'
y = map(lambda x: x.capitalize(), filter(lambda x: isinstance(x,str), my_items))
print(list(y))
print(Style.RESET_ALL)

a = issubclass(Employee, Employee)
print(a)

a = callable(show_list_items)
print(a)

a= p.Person('hersy',"hesltosn",18,["spanish"],"male")
b= hasattr(a,'name')
print(b)

my_items = 'hersy ', 20, 20.52, 'craice', True, 2j, 'ashley'
person=set()
total = 0
things=set()
for item in my_items:
    if isinstance(item, str):
        person.add(item.capitalize())
        continue
    
    if isinstance(item,(int,float)):
        total += item
        continue

    things.add(item)

print(Fore.GREEN + f"Grettings dears {person}")
print(Fore.BLUE + f"Total: {total:.2f}")
print(Fore.BLACK + f'Things: {things}')


    


    
