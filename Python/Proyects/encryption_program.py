import random as r
import string as s

chars:str = " " + s.punctuation + s.digits + s.ascii_letters
chars:list[str] = list(chars)
keys:str = chars.copy()
r.shuffle(keys)



#ENCRYPTIONS
print("enter a message to encript")
plain_text:str= "Craice support Hilther actions, i think she is out of her mind...."
chiper_text= ""

for letter in plain_text:
    index:int=chars.index(letter)
    chiper_text += keys[index]

print(f"your text: {plain_text}")
print(f"your chiper: {chiper_text}")
print()

#DESCRYPTIONS
print("enter a message to desencript")
dechiper_text:str= chiper_text
text:str= ""

for letter in dechiper_text:
    index:int=keys.index(letter)
    text += chars[index]
    

print(f"your chiper: {dechiper_text}")
print(f"your dechiper text: {text}")


# 
