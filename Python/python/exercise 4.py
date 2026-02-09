user_name = input("Greeting new user, please write your username: ")
if len(user_name) > 12:
    print("sorry new user, but the name you have written is too long")
elif not user_name.find(" ") == -1:
    print("i have noticed you just write a space, sorry but spaces are not allowed")
elif not user_name.isalpha():
    print("user i am afraid you have written numbers or special symbols, sorry, but it is not allowed neither")
else:
    print(f"welcome {user_name.capitalize()}! for us is a honor you are here.")



name  = input("write your username: ")
if len(name) > 10:
    print("write a lower name")
elif not name.find(" ") == -1:
    print("should not contain spaces ")
elif not name.isalpha():
    print("should only contain letters")
else:
    print(f"welcome {name} what are you up to...")

password = input("write a safe password")
print("you are registerd now" if len(password) > 8 else "password is too short")

sentence = input("write a short sentence: ")
result = sentence.find("love")
if result:
    print("i noticed you write love, that's cute")
else: 
    print("good sentence")

capitalize = input("write your name in lowercase: ")
result2 = capitalize.capitalize()
print(result2)

digital = input("write your age: ")
if not digital.isdigit():
    print("that is not a valid age, it is not even a number, what were you thinking, are you crazy...")
else:
    print(f"you are {digital}")

alpha = input("write your name: ")
if not alpha.isalpha():
    print("name only containts letters y'know, jerk!")
else:
    print(f"welcome abord {alpha}")

count = input("write another sentence: ")
result3 = count.count("e")
print(f"in this sentence you have written the letter e {result3} times!")


