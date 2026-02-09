#while loop = excute some code Whlesome condition remains True

age2 = int(input("enter your age: "))
if age2 < 0:
    print("you can't enter negative numbers ")
else:
    print(f"your age is {age2:>15}")

age = int(input("enter your age: "))
while age < 0 :
    print("you cannot enter negative numbers")
    age = int(input("enter your age: "))
print(f"your age is {age:>15}")




name = input("enter your name: ")

while name == "": #while this condition remains True will execute this code potentionlly forever
    print("your are not enter your name: ")
    name = input("enter your name: ")
    

print(f"Hello {name.capitalize(): ^15}")




food = input("Enter your favorite food (press q to quit): ")
while not food == "q":
    print(f"your like {food}")
    food = input("Enter your favorite food (press q to quit): ")

print("bye")

num = int(input("enter a number between 1 to 10"))
while num < 1 or num > 10 :
    print(f"{num} is not valid")
    num = int(input("enter a number between 1 to 10"))

print(f"your number is {num:^5}")