import math

while True:
    try:
        number = float(input('enter a number: '))
        break
    except ValueError:
        print('must be a valid quantity')

result = 2 * math.pi * number

print(f"your result is {result:,.2f}")

from operator import itemgetter

elements: list[int] = [1, 2, 3, 4, 5]
item: dict[str, int] = {'a':10, 'b':20, 'c': 30}
frist_and_last: itemgetter = itemgetter('a', 'c')

print(frist_and_last(item))