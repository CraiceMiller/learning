# colletion = list[], tuples(), sets{}

fruits = ['Apple', 'orange', 'banana', 'coconut']
fruits_2 = ['blueberry', 'raspeberry']
print(fruits[2])
print(fruits.index('banana'))
fruits.append('strawberry')
fruits.pop(0)
fruits.remove('banana')
fruits.insert(3, 'grape')
fruits.extend(fruits_2)
print(fruits)
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)

#fruits.clear()
if fruits == []:
    print('\nthere are not fruits')
else:
    print('\nThese are your fruits:')
    for i in fruits:
        i
        print(f'-{i}')

i = len(fruits)
print(i)
print(type(i))
print('\n')

# dictionaries
print('-------------------------------------------')
protagonist = {
    'Hollow knight': 'knight',
    'The legend of zelda': 'Link', 
    'Dead cell': 'Unhead',
    'Minicraft': 'steve'
}

print(protagonist.get('Dead cell'))

print('what protagonists game do you wnat to see ' )
attempt = input().lstrip().capitalize()

if protagonist.get(attempt) == None:
    print(f'there are no {attempt}, but we can add it, do you want to?:')
    answer = input().lstrip().lower()
    print()
    if answer == 'yes':
        print('so what is the main character?: ')
        new_character = input()
        protagonist[attempt] = new_character
        print()
        print('here is your new list')
        for key, value in protagonist.items():
            print(f" {key}: {value}")
        else:
            print('bye then.')
else: 
    print(f'yes {attempt} is within protagonist dictionary')
    print('its protagonits is :')
    print(protagonist[attempt])

decision = ['game', 'main']
print()
print('what do you want to see, the game or the main character?: ')
print('write game or main')
answer_2 = input().lstrip().lower()

while not answer_2 in decision:
    print('please write a valid input')
    print('write game or main')
    answer_2 = input().lstrip().lower()
    print()

print()
if answer_2 == 'game':
    print('here you go, these are the games at hand')
    for i in protagonist.keys():
        print(i)

if answer_2 == 'main':
    print('here you go, these are the main characters at hand')
    for i in protagonist.values():
        print(i)

print()
print('thanks to be here :)')