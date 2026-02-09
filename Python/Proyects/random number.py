import random

options: list[str] = ['lucky star', 'nazo no kanojo x', 'nichijou']
names:list[str, int] = [19, 'hersy', 18, 'craice', 17, 'ashley']

number: int = random.randint(1, 6)
number_2:int = random.random()
number_3:str = random.choice(options).capitalize()
number_4:str = random.shuffle(names)

print(names)