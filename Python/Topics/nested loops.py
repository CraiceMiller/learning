# nested loop = A loop within antoher loop
for i in range(2):
    for n in range(0,6):
        print(n, end='-')
    print('\n')


# retangule project

rows = int(input('enter the # of rows: '))
symbol = input('enter the symbol: ')
colums = int(input('enter the # of colum: '))

for i in range(rows):
    for x in range(colums):
        print(symbol, end='')
    print()

