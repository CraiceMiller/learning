# for loops = execute a block of code a fixed number of time.
#        you can iterate over a range(), string(), sequence(), etc.

print("firts example")
for x in range(1, 11 ):
    print(x)

for d in range(10):
    print(d)

days = ["monday", "thursday", "tuesday", "friday"]
for days in days:
    print(days)

print("second example")
for y in reversed(range(1, 11 )):
    print(y)
print("happy new year")


print("thrid example")
credit_card = "123-456-789"
for x in credit_card:
    print(x)
   
print("fourth example")
for i in range(1, 6):
    i = "everything's gonna be ok"
    print(i)

print("fith example")
for n in range (1, 11):
    if n == 7 :
        continue
    else:
        print(n)
        
print("sixth example")
for c in range (1, 11):
    if c == 7 :
        break
    else:
        print(c)
        
for num in range(1,6):
    print(num)

for letter in 'python is the best':
    print(letter)

colors = ['red', 'green', 'blue']
for colors in colors:
    print (colors)

for even_number in range(2,11,2):
    print(even_number)



name_1 = input('write a name: ')
name_2 = input('write a name: ')
name_3 = input('write a name: ')

names = [name_1, name_2, name_3]
for names in names:
    print(f"hello {names.capitalize()}, nice to meet you :)")



for banana in reversed("banana"):
    print(banana)
    

for x in range(1,11):
    if x == 5:
        break
    else: 
        print(x) 
    