# Input() : A funtion that prompts the user to enter data
#         Returns the entered data as a string

#the input always will be a string, so that's means if the user insert a number we need to convert whether a interger or a float
name = input("what is your name?:")  
print(f"hello {name}, what's going...") 
print("i am pretty sure we are gonna be besties :)") #since we're not inserting any variables, this doesnt need an F statement
age = input("btw, how old are ya?: ")
age = int(age)
age = age + 1 
print(f"you are {age} years old, so you're alredy a legal person..")
animes = int(input("how many animes have you seen so far?: "))
animes = animes * 2
print(f"so you have arleady seen {animes}, right? ")
print("since you're here. i can help you to calcute the area of a rectangle, wanna try")
lenght = float(input("well, this tell me the lengh: "))
width = float(input("now tell me the width"))
area = lenght * width 
print(f"so dude the answear of this is --{area}cm²--, arent i?") #² just type: alt + 0178  ²
item = input("what item d'ya wanna buy:")
print(f"ok, so it'll be {item} then")
price= float(input("and what is it the price of it: "))
print(f"got it worth ${price} for each")
quantity = int(input("and how many do you have to buy anyways: "))
total = price * quantity
print(f" so it will be ${total} wanna pay by credit card?.")

#____________________________________________________________________


  