# if: do some code only if some  condition is true
# else do something else
age = int(input("enter your age: "))
if age >=18:
    print(f"you are {age} you can enter")
elif age <= 2:                                 #it just add another statement
    print(f"you are {age} we dont want brats")
else:
    print(f"currently you are {age}, we don't wat kids")
respond = input("would you like some food Y/N: ")
if respond == "yes":
    print("have some food: ")
    list = input("what do you want to order: ")
    if list == "soup":
        print("got it,")
    else:
        print("we hardly recomend you the main dish, do you want: ")
        mind = input()
        if mind == "yes":
            print("here you go sr")
            dish = input()
            if dish == "thanks":
                print("you're welcome, ejoy your meal :)")
            else:
                print("at least you could say thanks, you know >:v")
        else:
            print("if you dont know yet here is the menu")
else:
    print("no food for ya: ")

online = True
if online:
    print("you are onlie")
else:
    print("you are NOT online")

hang_out = input("Dude, do you wanna hang out with me?: ")
if hang_out == "yes":
    print("i know you would say yes, so where do you want to go?(park, mall, beach): ")
    place = input("i would like to go to the  ")
    if place == "park":
        print("that sound goo")
    elif place == "mall":
        print("you too, actually i was planninhg to buy some of plushies...")
    elif place == "beach":
        print("you know what i am in, either way its scorching outside")
    else:
        print("that sounds boring, what about to the gym dude?")
else:
    print("why not, are you bussy")
    bussy = input()
    if bussy == "yes":
        print("gotcha, so i will no bother you anymore, bye")
    elif bussy == "()":
        print("please answer me dude...")
    elif bussy == "no":
        print("so, if you dont want to hang out, we can play videogame, shall we? ")
        game = input()
        if game == "yes":
            print("that great, what video game are you into nowdays (metrolvania, rpg, fight, shooters)")
            like = input()
            if like == "metrolvania":
                print("i heard those games are very tough...")
            elif like == "rpg":
                print("dudeee, i tried to play one of them one day but i bored so fast(why, what game did you play)")
                answer = input()
                if answer == "why":
                    print("why you ask?, well i think it is so slow you know")
                elif answer == "what game did you play":
                    print("have you heard this game called pokemon? (yes, no)")
                    poke = input()
                    if poke == "yes":
                        print("well the thing is i did love the little moster, but, gosh!!, the part i need to level up experiencia was a pain in the neck, you know")
                        level = input("(but i love it ,  i hate it too: )")
                        if level == "":
                            print("why dont say anything")
                        elif level == "but i love it":
                            print("i said i hate it, i meant i love it too... you dont belive me, right. ok i dont like it")
                        elif level == "i hate it too":
                            print =("yeah, fuck that game")

                    else:
                        print("you know what, it doesnt care, forget it") 
            elif like == "fight":
                print("you too, you have no idead how much time i used to play those games with my little brother")
            elif like == "shooters":
                print("i can tell you are war boy, dont get mad i just was kidding, you know")
            else:
                print("i dont heard about it, could you explain me? ")
        elif game == "no":
            print("if you dont want to, so what about do some of work out?")
    else:
        print("i dont get it dude...")