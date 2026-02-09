number = int = '10'
decimal = float = 10.50
text = str = 'Hello world!'
activate = bool = True

names : list = ['hersy', 'Craice', 'Ashely']
coordinate : tuple = (1.5, 2.5)
unique: set = {1, 4, 2, 7}
data: dict = {'name': 'hersy', 'Age': 18}






print('\n ------lists-----')
#lilsts
name = ['hersy']

name.append('craice') #we can add an items 
name.append('ashely')
#name.append(input("write a name: "))

print(name)
for i in name: #we can use the for statement
    print(f'hello {i.capitalize():^5}, nice to meet you')
    
print(name[2]) #we can use the indexing to watch an specific item

# name[2] = 'miseru' 
name.insert(2, 'miseru') #we can modify items

print(name)

others_names = ['mark', 'silver'] #we can add the values of one list from another
name.extend(others_names)
print(name)

# we can delate thing in a list 
# 1
name.remove('hersy') 
print(name)

#2
name.pop(0)
print(name)

# 3
name.clear()
print(name)




print('\n ------tuples-----')
# Tuples 
my_tuple = (1, 2, 3, 'hersy', 'craice', 4.23, True)
            
print(my_tuple[3])
print(f"your tuple is {my_tuple[-1]}")

for item in my_tuple:
    print(item)

numbers = (1, 2, (3, 'hersy'), 4, 'craice', ['ashely', 7, 8.50])
print(numbers[-1])

numbers[-1].append('miseru')


for z in numbers[-1]:
    print(z)




print('\n ------sets-----')
# set
colors = {'red', 'blue', 'green'}

colors.add('yellow')
colors.add('blue')
print(colors)
 
colors.remove('red')
colors.discard('purple')
print(colors)

for h in colors:
    print(h)

new_colors = {'black', 'gray', 'red', 'green'}
all_colors = colors.union(new_colors)

print(all_colors)
print(all_colors.pop())
print(all_colors)

print(colors.intersection(new_colors))
print(colors.difference(new_colors))
print(all_colors.clear())



print('\n ------dictionaries-----')
# dict
D = {1:10, 2:20, 3:30, 4:40}
print(D.get(2, 3))

student = ['hersy']
person = {
    'Name': 'hersy',
    'age': 19,
    'like': 'videogames'
}

print(person['Name'])
print(person.get(0))
print('\n')

person['city'] = 'Guatemala'

person['like'] = 'animes'
print(person)
print('\n')

person.pop('age')
print(person)
print('\n')

print(person.keys())
print('\n')
print(person.values())
print('\n')
print(person.items())
print('\n')
print(person.get('like'))
print('\n')
print(person.get('weight'))
print('\n')
person.update({'dislike': 'loliness', 'besty': 'miseru'})
print('\n')

for key in person.keys():
    print(key)
print('\n')
for value in person.values():
    print(value)
print('\n')
for key, value in person.items():
    print(f"{key}: {value}")


