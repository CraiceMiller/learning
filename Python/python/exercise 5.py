print(f"\n -------LISTS-------")
movies = ['sawV', 'black phone', 'MHA', 'kimetsu no kaiba', 'plundere']
print(movies)

#add
movies.append('jujutsu kaisen')
movies.append('sao')
print(movies)

#delete
movies.pop(1)
movies.remove('sao')
print(movies)

print(movies[-2:])

for i in movies:
    print(f"\n your favorite movie is: {i:^15}")

print(f"\n -------TUPLES-------")
fruits = ('banana', 'apple', 'strawberry')
print(fruits[1])

mixed = ('strawberry', [1, 2, 3], True)
mixed[1].append(4)
mixed[1].append('orange')
print(mixed)


countries = ('german', 'japan', 'mexico', 'usa', 'russia')
for i in countries:
    print(f"\n your contry is {i.capitalize()}")

print(f"\n -------SETS-------")
numbers = [1, 2, 2, 3, 3, 4, 5]
numbers = set(numbers)
print(numbers)

a = {1, 2, 3, 4, 7, 8, 9}
b = {3, 4, 5, 6, 4, 3, 4, 2, 10, 11}
print(a.union(b))
a.add(34)
b.add(124)
print(f"\n a to b")
print(a.intersection(b))
print(a.difference(b))

print(f"\n b to a")
print(b.intersection(a))
print(b.difference(a))

animes = {'jojos', 'najo no kanojo x', 'nijichou'}
animes.add('lucky star')
animes.add( 'call of the night')
print(f"\n {animes}")

animes.discard('jojos')
animes.discard('knj')
print(f"\n {animes}")

print(f"\n -------DICTIONARIES-------")
hersy ={
    'name': 'hersy',
    'age': 18,
    'language': ('spanish', 'english')
}

print(hersy['language'])
# i just want to do this
if len(hersy['language']) >= 2:
    print('\n you are a bilingue')
else:
    print(f"nice to meet {hersy['name'].capitalize()}")

hersy['age'] = 19
hersy['hobby'] = ['play videogames', 'hang out with friends']
hersy['dislike'] = {'loliness', 'complex stuff'}

for key, value in hersy.items():
    print(f"{key}: {value}")

student_1 = {
    'name': 'craice',
    'age': 19,
    'grade': ['A', 'A', 'B', 'A+']
    }

student_2 = {
    'name': 'ashely',
    'age': 18,
    'grade': ('C', 'B+', 'A-')
    }

student_1['friends'] = {'hersy', 'ashly', 'miseru', 'mark', 'dawnel' }
student_2['friends'] = {'hersy', 'craice', 'miseru', 'dayana', 'maurice', 'vanderiana' }
students = [student_1, student_2]

i = students[1]['name'].capitalize()
print(f"\nHello {i}")

a = students[0]['friends']
b = students[1]['friends']
all_friends = a.union(b)

print('\nList of friends: ')
for i in all_friends:
    print(f"- {i}")

x = a.intersection(b)
print(f"\n the students: {students[0]['name'].capitalize()} and {students[1]['name'].capitalize()} have this friends in common: {x} ")
print(a.difference(b))

besty = students[0]['friends'].pop().capitalize()
print(f"\n the besty of {students[0]['name'].capitalize()} is {besty}")

besty = students[1]['friends'].pop().capitalize()
print(f"\n the besty of {students[1]['name'].capitalize()} is {besty}")

print(f"\n -------STUDENTS-------")
for student in students:
    print(f"\n student: {student['name'].capitalize()}")
    for key, value in student.items():
        print(f"{key}: {value}")