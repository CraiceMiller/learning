# Nested = when one method is placed inside another. in other words
#  the ouput of one method becomes the imput for another.

name = 'hErSy'
print(name.lower().capitalize())


sentence = ' i love PROGRAMIN'
cleaned = sentence.strip().lower().replace('programin', 'anime').capitalize()
print(cleaned)

pass_word = input('write the password: ').strip()
while not pass_word == 'python':
    print('try again!')
    pass_word = input('write the password: ').strip()
print('o' + 'k ', 2)

user_name = input('write your name: ')