sunny = input("it is sunny: (yes, not): ")
go_out = input("do you wanna go (yes, not): ")
if sunny == "yes" and go_out =="yes":
    print("so lets go")
elif sunny == "not" and go_out == "yes":
    print("yeah i know yo wanna go but it is not sunny")
elif sunny == "yes" and go_out == "not":
    print("so what are you up...?")
elif sunny == "not" and go_out == "not":
    print("so lets play videogame intead")

age = int(input("what is your age: "))
member = input("are you a member(yes, not): ")
if age >= 18 and member == "yes":
    print("you can enter sr")
elif age < 18 and member == "yes":
    print("at leat you must have an adult with you")
elif age >= 18 and member =="not":
    print("if you dont have one, buy one there...")
elif age >= 18 or member == "yes":
    print("enter anyways")

password = input("what is the password (0001): ")
if not password == "0001":
    print("acces denied")
else: 
    print("because you are the best")

available = input("are you free(yes, not): ")
transportation = input("do you have any transportation(yes, not): ")
energy = int(input("1 to 10 how many energy you have today: "))
if available == "yes" and transportation =="yes" and energy >= 50:
    print("lets hang out")
elif available == "not" and transportation =="yes" and energy >= 50:
    print("maybe next time")