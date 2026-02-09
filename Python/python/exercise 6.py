# calculate the are of a rectangleM 1
def area_rectangle(lenght, width):
    result = lenght * width
    return result
lenght = 123.321
width = 987.789
print(f"your result is {area_rectangle(lenght, width):,.2f}, right")
print()

# calculate the are of a rectangle, 2
def area_rectangle(lenght, width):
    result = lenght * width
    return result
lenght = 123.321
width = 987.789
b = area_rectangle(lenght, width)
print(f"your result is {b:,.2f}, right")
print()

# greet a person, 1
def greet (name):
    name.lstrip()
    print(f"Hello {name.capitalize()}, nice to meet you")
greet ('hersy')

print()

# greet a person , 2
def greet (name):
   i = name.lstrip()
   i = name.capitalize()
   return i
z = greet ('hersy')
print(f"Hello {z}, nice to meet you")

print()

#even or odd 
def check(number):
    if number.isdigit():
        print('even')
    elif number.isalpha():
        print('odd')
check('12')
print()

#average of three
def average(a, b, c):
    i = (a + b + c) / 3
    return i
x = average(76, 80, 91)
print(f" the average is {x:,.2f}")
print()

# password, 1
def verify(word):
    a = 'python123'
    word = word.strip().lower()
    if word == a:
        x = print(f"Welcome back :)")
    else:
        x = print('Wrong!, try again')
    return x

verify(input('write the password: '))
print()

# password, 2
def verify_password(password):
    password = password.strip().lower()
    while not password == 'python123':
        print('Wrong!, try again')
        verify_password(input('write the password:'))
    print(f"Welcome back :)")

verify_password(input('write the password:'))






