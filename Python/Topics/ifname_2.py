# random fuctions 
def ok():
    #you program goes here
    for i in range(10):
        match i:
            case 5:
                break
            case _:
                print('everything\'s gonna be ok :)')

def food(f):
    print(f"you like {f}")

# greetings fuctins 
def greet()->None:
    print("hello master")

def bye()->None:
    print("Bye mater...")

def main()->None:
    greet()
    bye()


# club functions 
def is_an_adult(age:int,has_id:bool)->bool:
    return age >= 18 and has_id

def is_bob(name:str)->bool:
    return name.lower() == 'bob'

def club_members(member:list[str]) ->None:
    print()
    print("---club memebers-----")
    for name in member:
        print("- " + name.capitalize() )

def enter_club(name:str, age:int, has_id:bool)->None:
    names:list[str]=[]

    if is_bob(name):
        print("get out of my sight jerk!!")
        return 
    
    if is_an_adult(age,has_id):
        names.append(name)

        print("Hello " + name)
        print("you can enter the club")

    else:
        print("We sorry " + name + " but you can't enter")
        print("you can't enter in the club")

    print()

    if not names == []:
        club_members(names)


# 
def bank_users():
    data:dict[str,str]={"user_1":{"user": "Hersy",
                                   "money": 100.32},
                         "user_2":{"user": "Craice",
                                   "money": 652.98},
                         "user_3":{"user": "Ashley",
                                   "money": 48.5},}
    
    users:list[str] = [x for x in data]
    print(users)