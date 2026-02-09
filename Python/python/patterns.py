# partterns

# First try, triagle
for i in range(1, 5 + 1):
    for j in range(0, i):
        print("*", end = "")
    print()

print('\n')
for i in range(1, 6):
    print("*" * i)

print('\n')

# second try, triangle up

for i in range(6, 0, -1):
    for j in range(0, i ):
        print("*", end = " ")
    print("\r")



# third try, square

for i in range(0, 6):
    for j in range(10):
        print("*", end="")
    print()

print('\n')
# fourth try, pyramid

number= 2 * 5 -2
for i in range(6, 0, -1):
    for j in range(2, 0, -1):
        print(end = " ")
    number += 1
    for j in range(0, i +1):
        print("*", end= " ")
    print()
    
