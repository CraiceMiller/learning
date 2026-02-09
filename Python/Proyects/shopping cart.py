food = []
price = []
total = 0
food.append


while True:
    i = input("Enter a food to buy(press q to quit): " ).strip().capitalize()
    if i.lower() == 'q':
        break
    else:
        x = float(input(f'Enter the price of {i}: $ '))
        price.append(x)
        food.append(i)


print('------ YOUR CART-----')
for foods in food:
    print(foods.capitalize(), end=', ')
print()

for prices in price:
    total += prices

print(f'your total is ${total:,}')