import random
import time

print('python number guess')
print('\n')
time.sleep(3)

while True:
    lowest_num: int = 1
    highest_num: int = 50
    answer: int = random.randint(lowest_num, highest_num)
    guesses: int = 0
    is_running: bool = True

    while is_running:
        print(f"pick one number between  {lowest_num} and {highest_num}")
        print('enter your guess')
        guess = input()
        print()

        if guess.isdigit():
            guess:int = int(guess)
            guesses += 1

            if guess < lowest_num or guess > highest_num:
                print('that number is out of range')
                print(f"please, select one number between  {lowest_num} and {highest_num}")
            elif guess < answer:
                print('too low!!')
            elif guess > answer:
                print('too hight!!')
            else:
                print(f"correct the answer was {answer}")
                print(f"it took you {guesses}")
                is_running: bool = False


        else:


            print('Invalid guess')
            print(f"please, select one number between  {lowest_num} and {highest_num}")


    if not input('wanna continue [yes or not]...?: ').lstrip() ==  'yes':
        break

print('Thank for play')
print('\n') 
time.sleep(1)

for _ in range(1, 6):
    print('.', end = '')
    time.sleep(1)


print()
#-------------------------------
passes: bool = True
word: str = 'tamaki123'

while passes:
    pass_word: str = 'tamaki123'
    print('enter the password')
    attempt = input().lstrip()

    if  not attempt != pass_word:
        print('correct!!')
        passes: bool = False

    else:
        print('wrong try again')

print('\n')     

print('enter the password')
attempt = input().lstrip()
while attempt != word:
    print()
    print('Wrong!!!!, try again')
    print()
    print('enter the password')
    attempt = input().lstrip()
    

print('correct!!')