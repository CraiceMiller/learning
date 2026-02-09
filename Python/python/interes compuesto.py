def compuesto(capital:float = 200, interes:float=0.05, years:int=3)->None:
    result = capital *(1+interes) ** years
    print(f"Coumpond: {round(result, 2):,}$")
    
def simple(capital:float = 200, interes:float=0.05, years:int=3)->None:
    result = capital + (capital * interes * years)
    print(f"simple: {round(result, 2):,}$")


initial: float = float(input("enter you initial capital: "))

print("enter your interes then: ")
inter:float=float(input())
x = inter / 100


year:int=int(input("how many years?: "))

compuesto(capital=initial,years=year,interes=x)
simple(capital=initial,years=year,interes=x)