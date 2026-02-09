
my_dict={
    "a":[1,2,2,5,5,6,7,8,10,70.40,20,10],
    "b":["a","b","c",""],
    "c":[90.50,10,20,0],
    "d":["",0,[],0,""]
}

#enumerate
for n,i in enumerate(my_dict):
    print(i)
    print(i[0] == "b")

#isinstance, len, sum
def counter(values)->int|float:
    if isinstance(values[0],str):
        return len(values)
    return sum(values)

#map
print(list(map(counter,[items for items in my_dict.values()])))

#any, all
for items in my_dict.values():
    print()
    print(items)
    
    if all(items):#type: ignore
        print("All itmes are Trueness values")
        continue 

    if any(items):#type: ignore
        print("There is at leat one True value")
        continue 


    print("all the itmes are falsy ")

#zip
for a,b in zip([1,2,3],[10,20,30]):
    print(a,b)

#filter, lambda
numbers:list=list(filter(lambda x: isinstance(x[0], int|float),my_dict.values()))#type: ignore
list_number:list=[]

for num in numbers: 
    list_number.extend(num)

#sorted 
print(sorted(list_number,reverse=True))
print(f"Minimun number {min(list_number)}")
print(f"Maximun number {max(list_number)}")

#set
unique_numbers:list=list(set(list_number))
print(unique_numbers)

#round, sum
print(round(sum(unique_numbers) / 7,2))

print()
#reversed 
for value in reversed(unique_numbers):
    print(value)
print()

#abs
negative_number:int=-10
number: int =7
print(f"Result without abs: {number + negative_number}")
print(f"Result with abs: {number + abs(negative_number)}")
print()


#callable 
print(f"If counter callable?: {callable(counter)}")
print(f"If negative_number callable?: {callable(negative_number)}")
print(f"If abs callable?: {callable(abs)}")


#callable and zip 
functions_:list=[counter,negative_number,abs,]

for fun in functions_:
    print(callable(fun))

#range
def display_message(message:str,times:int=3)->None: 
    for text in range(times+1): print(message)

display_message("Everyting's gonna be okay")

#pow 
def power(number,times=2)->int:
    return pow(number,times)
print(power(7))










"""
my_dict={
    "a":[1,2,2,5,5,6,7,8,10,70.40,20,10],
    "b":["a","b","c",""],
    "c":[90.50,10,20,0],
    "d":["",0,[],0,""]
}

for index, item in enumerate(zip(*my_dict.values())):
    print()
    print(index,f"{item}")

print()
print(list(zip(my_dict.values())))
print(list(zip(*my_dict.values())))
print()

"""

