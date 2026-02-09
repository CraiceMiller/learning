import functools 

# lambda statement it is the same to use fuctions

x = lambda a,b:(a+b)**2

print(x(1,4)) # output:25

def y(a,b):
    return (a+b)**2

print(y(1,4)) # output:25

print((lambda x,y:(x+y)**2)(1,4) ) # output:25




# when we use map() it is the same to use 'for' statement 
i = [1,2,3,4]
squares = []

for square in i:
    squares.append(square**square)
print(squares) # output: [1, 4, 27, 256]

squares_2= list(map(lambda square:square**square,i))
print(squares_2) # output: [1, 4, 27, 256]

squares_3=[(lambda x:x**x)(i) for i in range(1,5)]
print(squares_3) # output: [1, 4, 27, 256]

#what i  am saying is firt the variable squares_2 it will be a list due the list()
#then we are saying for when we type map()
# lambda square is the same as: for square
# the folling state after the 'lambda' is the same as how a 'for' statement works 
# and the end of the lambda we write a group (or a iterable object), 
#for square in i:... == map(lambda square:...,i)


#when we use filter() it is the same to use a list comprehesion 
my_numbers= [1,2,3,4,5,6,7,8,9,10]
evens=[x for x in my_numbers if x % 2 == 0]
print(evens) #output: [2, 4, 6, 8, 10]

evens_2=list(filter(lambda x: x % 2 ==0,my_numbers))
print(evens_2) #output: [2, 4, 6, 8, 10]

evens_3=lambda x: x % 2 ==0
print(evens_3)


# sorted(), this is like a filter, if we sored something using a specific value whithin it
students = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

names=[("Hersy", "matt",90 ),("Ashly", "Darwing",85),("Craice","elizabeth",76)]
number=[5,8,1,2,9,4]
number.sort(reverse=True)
grade = sorted(names,key=lambda n:n[2])


sorted_students_by_age = sorted(students, key=lambda x: x["age"], reverse=True)
print(sorted_students_by_age)

print(sorted(names))
print(number)
print(grade)

# this is almost the sames like 'for' statement 
list_numers=[1,2,3,4,5,6]

sum_numbers=functools.reduce(lambda acc,x:acc+x, list_numers)
print(sum_numbers) # output: 21

add_numbers=0
for j in list_numers:
    add_numbers+=j
print(add_numbers)  # output: 21

z = (((((1+2)+3)+4)+5)+6)
print(z)# output: 21

# with only two value we can use this 
c,r=1,6
print(c) if c > r else print(r)  # output: 6

# but in a group we need to use reduce() function 
max_number=functools.reduce(lambda c,r:c if c>r else r, list_numers)
print(max_number) # output: 6

print(functools.reduce(lambda c,r:c if c>r else r, list_numers)) # output: 6

# to sum up. lambda statement could be a replace of for, def and if statment. if only the code could be written in one silge onlie otherwise we need to use the previous statements 
