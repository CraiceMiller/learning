#13/june/2025
import random
# create a slot
# this slot must to contanit the value in real  time 



def bank(num:float = 100.0) -> float:
     return num


total = round(0,2)
money= 0

print("How much do you wanna lost- I mean invest: ")
money = input()

while not money.isdigit():
  money = input()

money = float(money)
total += money


while True: 
        num_1 = random.randint(0,7)
        num_2 = random.randint(0,7)
        num_3 = random.randint(0,7) 
       
        print("------------------ SLOT -----------------------")
        print(f"current money:")
        print(f"${round(total,2)}")
        print()
    
    

    
            
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
if total <= 20:
    print(f"you final amount: ${total:.2f}")
    print("i can't believe you lost so many money")
else:
     print(f"you final amount: ${round(total,2)}")