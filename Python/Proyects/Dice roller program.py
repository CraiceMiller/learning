import random
import time



# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art: dict = {
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘" ), 
    2:("┌─────────┐",
       "│  ●      │",
       "│         │",
       "│     ●   │",
       "└─────────┘" ), 
    
    3:("┌─────────┐",
       "│      ●  │",
       "│    ●    │",
       "│ ●       │",
       "└─────────┘" ), 

    4:("┌─────────┐",
       "│ ●     ● │",
       "│         │",
       "│ ●     ● │",
       "└─────────┘" ), 

    5:("┌─────────┐",
       "│ ●     ● │",
       "│    ●    │",
       "│ ●     ● │",
       "└─────────┘" ), 

    6:("┌─────────┐",
       "│ ●     ● │",
       "│ ●     ● │",
       "│ ●     ● │",
       "└─────────┘" )


}

dice_list: list[int] = []
total: int = 0
print('how many dices do you want')
num_of_dices: int = int(input())

for dice_loop in range(num_of_dices):
    dice_list.append(random.randint(1, 6))




#for dice in range(num_of_dices):
 #   for line in dice_art.get(dice_list[dice]):
  #      print(line)

for loop_of_lines in range(5):
    for dice_print in dice_list:
        print(dice_art.get(dice_print)[loop_of_lines], end= "  ")
   
    print()


for sum_of_total in dice_list:
    total += sum_of_total


print()
print('total:', total)
