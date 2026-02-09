
weight = float(input("enter a number: "))
unit = input("enter a unit (Kg or L): ")

if unit == "Kg":
    weight *= 2.205
    unit = "Lbs"
elif unit == "L":
    weight /= 2.205
    unit = "Kg"
else:
    print(f"{unit} is not valid")

print(f"your weight is {round(weight, 2)}{unit}")