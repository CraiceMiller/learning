from functions_to_use import get_speech_input


if __name__ == "__main__":
    #this is the part i add myself
    user_=get_speech_input()
    if "python" in user_:
        print("- {}".format(user_))
        print("You said something about Python and you know what I love Python too!!")
    elif user_=="school":
        print("don't say it, cuz i hate it...")
    elif user_=="":
        print("it seem, has occured an error...")
    else:
        print(f"You said {user_}")