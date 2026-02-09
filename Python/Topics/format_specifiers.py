# format specifier = {:flags} format a value based on what flags are inserted
name = "hersy"
number = 12345.6789
name = name.capitalize()
print(f"Your name is: {name:>10}")
print(f"Your name is:{name:10}")
print(f"Your name is: {name:<10}")
print(f"Your name is: {name:^10}, right or are you craice?")
print(f"Your name is: {name}")
print(f"This is your number: {number:.3f}")
print(f"This is your number: {round(number, 3)}")
number = round(number, 3)
print(f"{number:,}")
print( number + 4)
print(f"This is your number: {number:,}")
print(f"This is your number: {number:+}")
print(f"This is your number: {number:10}")
print(f" your number: {number:>15,.2f} and your name: {name:^5}")
#_____________________________________________________________________________________

product = "laptop"
price = 999.499
stock = 2500
rating = 4.7364

product = product.capitalize()
print(f"Product: {product:>10}")
print(f"Price: {price:+2}")
print(f"Stock: {stock:>12,}")
print(f"Rating: {rating:^10.3f}")
print(f"{"AVAILABLE":^20}")




price1 = 112312.3535
price2 = "5456.356"
price3 = 1002202

 
print(f"{price1:^}")
price2 = float(price2)
print(f"this is the price ${round(price2, 2)}")
print(f"this is the price ${price3:,}")


# > = this just move towards right
# < = this just move towards left