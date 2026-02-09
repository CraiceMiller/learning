
number_1 = float(input("enter the first number: "))
operator = input("enter a siganal; ")
number_2 = float(input("enter the second number: "))

if operator == "+":
    result = number_1 + number_2
    print(round(result,  2))
elif operator == "-":
    result = number_1 - number_2
    print(round(result, 2))
elif operator == "*":
    result = number_1 * number_2
    print(round(result, 2))
elif operator == "/":
    result = number_1 / number_2
    print(round(result, 2))
else:
    print("please enter a valid number")
