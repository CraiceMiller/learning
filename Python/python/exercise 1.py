import math

radius = float(input("please write the radius: "))

c =2 * math.pi *  radius

print(f"so the answear is {round(c, 2)} cm², right")
 
area = float(input("write the area: "))

a = math.pi * pow(area, 2)

print(f"my dear, this is your answear?, {round(a,2)} cm²")
s = input()
print(f"i am happy i could be able to help :)")

number = int(input("write a number"))
number *= 2
print(f"so this is your result {number}")

print("now it is moment to another question")
x = int(input("now write a number to add"))
y = float(input("then write another number"))
x += y
print(x)
x2 = int(input("now write a number to divide"))
y = float(input("then write another number"))
x2 /= y
print(x2)
x3 = int(input("now write a number to minus"))
y = int(input("then write another number"))
x3 -= y
print(x3)
x4 = int(input("now write a number to power"))
y = float(input("then write another number"))
x4 **= y
print(x4)

print("you are doing awesome dude, let's keep going")
s = float(input("write a number with decimals"))
t = float (input("now write another number"))
r = round(s)
r1 = abs(t)
r2 = max(s, t)
r3 = min(s, t)
r4 = pow(s, 2)
r5 = pow(t, 4)
print(r)
print(r1)
print(r2)
print(r3)
print(r4)
print(r5)

input("wanna continue?")
print("incredibly you are doing great here, let's with onether one")
re = float(input("now write a number to know the area"))
ro = float(input("another"))
ans = 1/2 * re * ro
print(f"so the answer is {round(ans, 2)}cm², i told you i am so smart >:v ")

