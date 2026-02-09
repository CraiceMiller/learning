import random
# create a slot
# this slot must to contanit the value in real  time 
#create your bank account, with the aim the person just can withdraw money within it


def bank(num:float = 100.0) -> float:
     your_money:float = num 
     return your_money


total = round(0,2)
while True: 
        num_1 = random.randint(0,7)
        num_2 = random.randint(0,7)
        num_3 = random.randint(0,7) 
        money= 0
        print("------------------ SLOT -----------------------")
        print(f"current money:")
        print(f"${round(total,2)}")
        print()
    
        
        print("How much do you wanna lost- I mean invest: ")
        money = input()

        while not money.isdigit():
            money = input()

        money = float(money)
        total += money 

    
            
        print("---------------------------")
        print(num_1, end=" ")
        print(num_2, end=" ")
        print(num_3, end=" ")
        print()
        print("---------------------------")


        if num_1 == num_2 and num_1 == num_3:
                print("you lucky bastard ")
                total = total * 2
        elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
                print("Nice!!")
                total = total + (total * 0.25)
        else:
            print("Too bad !!")
            total=total - (total* 0.75)
        
        print(f"current money:")
        print(f"${round(total,2)}")
        print()

        
            
        print("Are you satisfatied with that: ")
                
        again = input().lstrip().lower()
        if again == "yes":
            break
        else:
            pass
        
print()
if total <= 0:
    print(f"you final amount: ${total}")
    print("i can't believe you lost so many money")
else:
     print(f"you final amount: ${round(total,2)}")