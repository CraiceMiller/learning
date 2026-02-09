text:str="Everything is gonna be okay"
from time import sleep
for _ in range(100+1):
    print(text, end=" | ", flush=True,sep="_")
    sleep(1.5)