
unit = input("is this tempature calsisu or pahrenhelts? (C, F): ")
temp = float(input("Enter the tempature: "))

if unit == "C":
    temp = (temp * 9) / 5 + 32
    unit = "°F"
    print (f"your result in pahrenhelts is {round(temp, 2)}{unit}")
elif unit == "F":
    temp = (temp - 32) * 5 / 9
    unit = "°C"
    print(f"your tempeture in celsisu is {round(temp, 2)}{unit}")
else:
    print (f"Erro 404, {unit} or {temp} is not a valid variable")
    