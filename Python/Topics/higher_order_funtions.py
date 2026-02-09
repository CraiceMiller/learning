def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)

print(divide(10))
print(divide(5))

print(divide(127))

#
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def texting(funct, text:str):
    x = funct(text)
    return x

y = texting(loud,"I am hersy :)")
z= texting(quiet,"SHUTT YOUR PIE HOLE!!...")
print(y)
print(z)

# 
def additor(a):
    return a

def addited(c):
    return c**2

def adittion(a,c):
    a= additor(a)
    c= addited(c)
    return a +c

z=adittion(2,5)
print(z)

#
def greet(text:str):
    def name(n:str):
        return text + " " + n.capitalize() + ", today it's a nice day :3"
    return name

salutation = greet("Good morning")
print(salutation("master"))
print(salutation("hersy"))

night= greet("Good night")
print(night("craice"))