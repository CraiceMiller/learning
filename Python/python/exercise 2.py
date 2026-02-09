import math
print("oh, good afternoon sir, what d'ya wanna but today :)")
item = input("well, i'd like to buy ")
price = input(" that worth $")
item2 = input("and ")
price2 = input(" that worth $")
item3 = input("and ")
price3 = input(" that worth $")
print("ok sr, lemme check these out")
total = float(price) + float(price2) + float(price3)
print (f"it'll be ${round(total,2)}, how many items do you want")
q = int(input())
if q >=4:
    print("you lucky guy, since you buy more than 4 items we're gonna give ya a discount")
    total_discount= total * 0.20
    final_total= total - total_discount
    print(f"the total will be ${round(final_total)}, ")
else:
    print("ok, sr, here you go")
print("in short you're gonna buy...")
print(item)
print(item2)
print(item3)
print("have a nice day :)")