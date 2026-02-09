import time
def countdown(number) -> None:
    for x in range(number,0,-1):
        seconds: int = x % 60
        minutes: int = int(x / 60) % 60
        hours: int = int((x / 3600))
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
    print("Time is up")



want_countdown: str = input("do you want a countdwon?[yes, no]; ")
while True:
    
    if want_countdown == "yes":
        print("ok what is the time at hand")
        number = input()
        while not number.isdigit():
            print("please write a valid number:")
            number = input()
        number = int(number)
        countdown(number)

        print()
        print("do you wanna anoter countdwon?: ")
        again = input()
        if again == "yes":
            pass
        else:
            break
    else:
        break

print()
print("i hope you like it")