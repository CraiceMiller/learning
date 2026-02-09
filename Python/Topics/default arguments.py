#default arguments = A default value for certain parameters
#                    default is used when that argument  is omitted
#                    make your funtions more flexible, reduce # of arguments
#  positional, default, keyword, arbitrary 

# positional
def introduce(name: str, age: int)-> None:
    name = name.capitalize()
    print(f"Greeting {name} with {age} years old, I'm quite sure we will get along")

introduce("hersy", 18)

#2
def rectangle_area(length:float, width: float ) -> float:
    return round(length * width, 2)

print(rectangle_area(25.25, 5))

#default 
def greet_user(name: str = "Guest", languague:str = "English")->  None:
    print(f"Hello {name}, you can speak {languague}")


print("Write your name(optional)[type enter to pass]")
name = input().lstrip().capitalize()
print()

print("Write your languague(optional)[type enter to pass]")
languague = input().lstrip().capitalize()
print()
if name =="" and languague =="":
    greet_user()
elif languague == "":
    greet_user(name)
elif name == "":
    greet_user("Guest", languague)
else:
    greet_user(name, languague)

#2
def envoice(price:int = 100, disccount: float = 0.25)-> float:
    return round(price * disccount, 2)

print("What is the disccount?(optional)[press enter to pass]")
disccount = input()

print(envoice()) if disccount == "" else print(envoice(float(disccount)))

print()
# keyword
def register_user(name:str, role:str , level:int , currency: float)-> None:
    print(f"[{name}] has been register as a {role}, level: {level}, currently they have ${currency}")
    print()


register_user(name="Megumi",
              currency=99.50,
              level=20,
              role="magician"
              )


register_user(role="swordman",
              name="Tanjiro",
              currency=99.50,
              level=45
              )

#2
def travel(destination:str, duration:str)->None:
    print(f"the travel of {destination} will be within {duration}")
    print()

travel(duration="5 days",
       destination="Japan")

travel(duration="4 days",
       destination="Russia")

# artitrary

def add_numbers(*numbers: int) -> None:
    for i in numbers:
        print(i, end="-")
    print()
    print(type(numbers))
    total = sum(numbers)
    print(f"Total: {total}")
    
add_numbers(1,2, 4, 6, 7,8)
print()

#
def profile(**values) ->None:
    print(type(values))
    print()
    for key, value in values.items():
        print(f"{key}: {value}")
    print()

    wanna_know= "family"
    print("there is no  that element here") if values.get(wanna_know) == None else print(values.get(wanna_know))


profile(name="hersy",
        age= 18,
        country="Altisora",
        friends=("ashley", "craice"))
    
#
def list_items(*item):
    print("items at hand")
    for i in item:
        print(i, end=",")
    print()

    print(item[-1])

list_items("banana", "coconut", "grape", "apple")
print()

#
def format_message(**parts):
    print(f"from: {parts.get("sender").capitalize()}")
    print(f"Receiver: {parts.get("receiver").capitalize()} ")
    print(f"Date: {parts.get("date")}")
    print(parts.get("text"))
    print(f"Place. {parts.get("place")}")


format_message(sender="hersy",
               receiver="craice",
               text="what's up dude, y'know, we're gonna throw a party, and we're wanna you'll be able to be there",
               date="Today :)",
               place="a house, obviously,dammy :3")

def add(*args:tuple)-> int:
    total:int = 0
    for i in args:
        total += i
    return total

print(add(1,4,6,8,5))

def display_name(*full):
    for i in full:
        print(i, end=" ")

display_name("Lic.", "Craice", "Wilthon")
print()

#
def print_address(**kwargs):
    for i in kwargs.values():
        print(i, end=" ")

print_address(street= 123,
              city= "Altisora",
              state="M12")

print("\n")
#
def student(*args:tuple, **kwargs:dict)->None:
    for i in args:
        print(i, end=" ")
    print()

    for j in kwargs.values():
        print(j, end=" ")
    print()
    print()

    print(f"{args[0]}: {kwargs.get("name")}")
    print(f"Courses: {kwargs.get("courses")}")

    if "average_notes" in kwargs:
        print(f"Average note of {kwargs.get("name")} is: {kwargs.get("average_notes")} ")
    else:
        print(f"{kwargs.get("name")} is a good students")
    print()


student("Student", "High school",
      name = "Ashley",
      room_class = "C-2",
      courses = ("math", "art", "accounting"))

student("Student", "High school",
      name = "Criace",
      room_class = "D-2",
      courses = ("taxes", "management", "development"),
      average_notes=94.44)