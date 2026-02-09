import banking_program as bk

def customer():
    pass

products = {
    'consoles': 299.99,
    'digital games': 64.95,
    'physical games': 79.99,
    'plushies': 30,
    'controls': 43.95,
    'suscription': 19.99,
    'shirts': 14.95,
    'mysteious boxes': 24.45
}

cart = []
total = 0

print('------------PRODUCTS------------')
print()
for key, values in products.items():
    print(f"{key:.<25}${values:.2f}")
print('\n')

while True:
    print('Dear customer what do you want to purchase?(x to quit): ')
    purchase = input().lstrip().lower()
    if  purchase == 'x':
        break
    elif products.get(purchase) is  None:
        print("please enter a valid input")
    else: 
        print('that great, Keep order whatever you want::\r ')
        cart.append(purchase)
        print()
    
    
print()

print('------------ORDER------------')
print('these are the items you wanna buy')
for purchase in cart:
    total += products.get(purchase)
    print(purchase, end=" ")
print()

print(f"the total amount will be ${total:,.2f}")
print("we will wait for your pay...")


print(f"in your waller have: ${bk.my_wallet()}")

pay=float(input())

while not  pay in range(int(bk.my_wallet())):
    print(" or wanna try debit card instead:")
    chosse=input().lower().lstrip()
    if chosse == 'yes':
        pay = float(input())

    else: 
        print(f"in your waller have: ${bk.my_wallet()}")
        pay=float(input())

        break
        

    
final_purchase = pay - total

if final_purchase < 0:
    print("you dont have suffecient money to buy ")
    print("Wanna use your credit card")
    i = bk.credit_card()

    x = bk.my_wallet() + i 

    if x < total:
        print("you still to pay more")

    

else:
    print("here you go, your stuff!!, have a nice day ")

            

