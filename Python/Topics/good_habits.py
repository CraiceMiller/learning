# 1: if __name__ == '__main__':
# 2: main(): Just gather all the info in one single block 
# 3: big funtions: turning into smalls and reausable block
# 4: type anotations 
# 5: lists comprehesions 

import ifname_2 as ie

#1 and 2
if __name__ == '__main__':
    ie.main()



#3
print()
ie.enter_club("hersy",18,False)
ie.enter_club("Craice",19,True)
ie.enter_club("Ashely",17,True)
ie.enter_club("Bob",25,True)


# 4 and 5
def numers(num:list[str])->None:
    print("Even numbers")
    print([x for x in num if x % 2 == 0])
    
    print()
    print("square of even numbers")
    print([x**2 for x in num if x % 2 == 0])

example:list[int] = [1,2,4,5,6,8,"hersy"]

print()
try:
    sum(example)
    numers(example)
except TypeError:
   print("only numbers!!")