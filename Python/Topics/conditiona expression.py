# conditions expression = a oline shorcut for the if-else statment
# print or assign one of two values basedon a condition 
# x if condition else y 

num = 5
num3 = 5
print("enter" if num > 0 else "not enter")
if num3 > 0:
    print("enter")
else:
    print("no enter")

a = 6
b = 8
max_num = a if a > b else b
ab = max(a, b)
print(max_num)
print(ab)


temp = 30
is_raining = False

if temp > 35 or temp < 0 and is_raining:
    print("the outdoor event is call off")
else:
    print("the outdoor event is keep going")

print("the outdoor event is call off" if temp > 35 or temp < 0 or is_raining else "the outdoor event is keep going")





name = "bro"
name2 = "due"
print("hello" if name == "dude" else "who are you")
if name2 == "dude":
    print(f"hello {name2} how are you ")
else:
    print(f"{name2}? who are you ")


num2 = 6
result = "even" if num2 % 2 == 0 else "odd"
print(result)

age = 20
print ("Adult" if age >= 18 else "brat")

score = 86
res = "passed" if score > 70 else "falied"
print(res)

number = 43
print("even" if number % 2 == 0 else "odd")

age2 = 23
print("adult" if age2 > 18 else "kid")

temperature = float(input("enter temperature"))
print("it is hot" if temperature > 30 else "it is not hot")

score = int(input("enter your score: "))
print("passed" if score < 60 else "failed")

x = 10 
y = 20
maximun = x if x > y else y 
print(f"this is the greater number {maximun}")