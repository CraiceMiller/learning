# Typercasting = the process of converting a variable from one data type to another
#                str(), int (), float(), bool()
# to convert one type of value into another type of value; convert the string data itno integer data

name = "Dude" 
age = "18"
place = 44.6432
is_student = True 

age = str(age)
print(f"I am {age} years old" )
#-----------------------------------------
number1 = "25"
number2 = "30"

result = int(number1) + int(number2)
print(result)
#-----------------------------------------
price = float("3.60")
worth = 4.60
full = 5

total = price + 1.25
print(total)

total2 = worth + 2.60
print(total2)

total3 = int(worth) + 2.60
print(total3)

total4 = float(full) + 3.76
print(total4)

total5 = int(float(price)) + full + int(worth) + 1.25
print(total5)

print(type(total5))
#-----------------------------------------


# this is just to know what kind of variable is
#print(type(name))
#print(type(age))
#print(type(place))
#print(type(is_student))