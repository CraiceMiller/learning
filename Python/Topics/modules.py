# modules = a file  containing code you want to include in your program
#           use 'import' to include a module ( built -in or your own)
#           useful to break up a large program reusable separte files

import math 
import funtion_def 
import example_modules as e
from time import sleep

#
square = math.sqrt(25)
radius:float= round(math.pi * pow(7,2), 2)

print()
print(radius)
print(round(square,2))
print()

#
e.ok()
e.nothing()
print()



#
for i in range(2):
    print(i)
    sleep(1)



#
print(funtion_def.numbers(5,6))
funtion_def.full_name("hersy", "helston")
funtion_def.birthday("ashely", 19)
print()
funtion_def.display_invoice("hersy", 55, "buy a manga")

print()
