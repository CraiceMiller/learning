#2/8/25
from functions_to_use import palindrome, get_target_number
words:list=["aidia","Level","banana","duck","Nun","clock","Eve","mouse"]
palindrome_words:list=list(filter(palindrome,words))
for index,w in enumerate(palindrome_words,1):
    print(f"Word NO.{index} {w}")
   

numbs:list=[1,2,8,9,19,7,6]
num_target:int=15
verification:tuple=get_target_number(numbs,num_target)
if verification !=():
    print(f"these number: {verification} sum {num_target}")
else:
    print("no numbers found")
