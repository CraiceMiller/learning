principle = 0
rate = 0
time = 0

while True:
    principle = float(input("enter the principle amount: "))
    if principle < 0:
        print("principle can't be less than 0")
    else:
        break

while rate <= 0:
    rate = float(input("enter the rate amount: "))
    if rate <= 0:
        print("rate can't be less than 0")


while True:
    time = int(input("enter the time: "))
    if time < 0:
        print("time can't be less than 0")
    else:
        break

result = principle * pow((1 + rate / 100), time)
print(f'{result:,.2f}')
print(round(result, 2))
   
