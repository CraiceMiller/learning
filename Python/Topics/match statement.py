#match statement = AN ALTERNATIVE TO USING MANY 'IF' STATEMENTS
#                  execute some code if a value matches a 'case'
animes:list[str] = ["Nazo no kanojo X", "Jojo's", "Nichijou", "Azumanga", "domestic no kanojo"]

def is_anime(anime) -> bool:
    match anime:
        case "banana":
            return False
        case "Nazo no kanojo X"| "Jojo's"  | "Nichijou"| "Azumanga"| "domestic no kanojo":
            return True
        case "Jhon Wick" | "Encanto" | "Downfall":
            return False
        case _:
            return False


x = is_anime("Nazo no kanojo X")
print("let's be friends" if x else "Dont talk to me anymore!")
print()

#2
def grade(num)->str:
    print(f"you grade: {num}")
    try: 
        match num:
            case num if num >= 90 :
                return"you are doing great"
            case num if num >= 80:
                return "you still have a good grade "
            case num if num>=70:
                return "you can improve"
            case _:
                return "you lost the course!!!"
           
    except TypeError:
        return "is not a valid grade, dude"
        
print(grade("math"))
print()
print(grade(55))
print()

#3
def fruit_list(item)->str:
    print(item)
    
    match item:
        case "banana" :
            return "banana is full of potassium"
        case "apple":
            return "apple keeps doctor away"
        case _:
            return "it is not my bascket"

print(fruit_list("apple"))
print()

#4
def day_of_the_week(day)->str:
    match day:
        case "monday":
            return "back to school"
        case "friday":
            return "it is almost weekend"
        case "saturday"|"sunday":
            return "it is WEEKEND!!!!"
        case _:
            return "it is just normal day"
        
week = ("monday", "tuesday", "wednesday", "thrusday", "friday", "saturaday", "sunday")

x = "pizza"
while x not in week:
    print("Write a day")
    x = "saturday"
    break

print(day_of_the_week(x))

#5
def command(button)->str:
    match button:
        case "start":
            return "starting engine..."
        case "stop":
            return "engine stopped"
        case "pause":
            return "game pasued"
        case "exit":
            return "end of the program " 
        case _:
            return "unknow command "

print(command("start"))
print()

#6
def math_operator(num_1:float,operator:str,num_2:float)->float:
    match operator:
        case "+":
            return num_1 + num_2
        case "-":
            return num_1 - num_2
        case "/":
            try:
                return  num_1/num_2
            except ZeroDivisionError:
                return "you are operating with zero"
        case "*":
            return num_1*num_2
        case _:
            return "there is an invlaid input"
            
print(math_operator(num_1=5.5,operator= "/",num_2=0))
print()



#//////////
number_list:list[int]=[]

for i in range(10):
    number_list.append(i)

print([x for x in number_list])
print()
print([x for x in number_list if x % 2==0])
print()
print([x*2 for x in number_list])
print()

#//////

try:
    x=int(5)
    print(x * x )
except ValueError:
    print("write a number")