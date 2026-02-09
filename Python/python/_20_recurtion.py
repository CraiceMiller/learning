
def factorial(n):
  if n == 1: return 1

  return n * factorial(n-1)

print(factorial(5))


def walk(steps): 
  if steps == 0: return 

  walk(steps-1)
  print(f"You took one step. No.{steps}")

def multiply(number:int): 
  if number >=10: return 

  print(number)
  return multiply(number*1)

multiply(5)




walk(5)
print()
