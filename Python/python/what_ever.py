import math

x = 0
y = 45
print(x if not x <45 else y)
print("ok" if  x > 5 and y < 80 else "no ok")
print("ok" if  x < 5 or y < 80 else "no ok")



width = float(input("please add the width: "))
length = float(input("please add the length: "))
result_2 = width * math.pi * pow(length, 2)
final_result = round(result_2, 2)
print(f"{final_result:,}")

i = input("write a number below to 10: ")

while not i.isdigit():
    print("please write a number.")
    i = input("write a number below to 10: ")

i = int(i)

while i >= 10:
    print("please write a number less than 10")
    i = input("write a number below to 10: ")



i = int(i)

while i < 10:
    print(i)
    i += 1


password = input("write the password: ")
while not password == "python":
    print("wrong!, try again.")
    password = input("write the password: ")
print("acces allowed")

positive_number = input("wrte a positive number: ")
while "-" in positive_number or not positive_number.isdigit():
    print("just positive numbers are allowed, try again.")
    positive_number = input("wrte a positive number")
positive_number = int(positive_number)
print(f"your number is {positive_number:+,} ")

anime = input("dude, what is your favorite anime?: ")
while not anime == "exit":
    print(f"your favorite anime is {anime:^15}, me too!")
    anime = input("what others animes do you like?: ")
print("ok then bye ")

x = 0
while x <= 10:
    print(x)
    x += 1

y = 10
while y >= 0:
    print(y)
    y -= 1
    

i = 8 % 2 == 0
print(type(i))
i = int(i)
print(type(i))

