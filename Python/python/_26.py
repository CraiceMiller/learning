from time import localtime, perf_counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from threading import Thread

t=datetime.now().hour

print("Hello World!")

def f()->None:  

    h=datetime.now().hour
    h2=localtime().tm_hour

    print("The time right now: ", h)
    print("The time right now: ", h2)

def h(n)->None: 
    text=""
    for _ in range(100_000_000): 
        text = "Hello World! "
    print(text)
    print(f"Hello No. {n}")


def g()->float: 
    from random import randint
    n=0
    a=10
    b=0
    global t
    if "Hello" == "Hello": 
        if n ==0: 
            if True: 
                if n < a: 
                    if a == b: 
                        if a != n: 
                            if not False:
                                if t == 12:
                                    if 100 > a: 
                                        if n < t:
                                            if (100 / 2) == 50: 
                                                if True and not False: 
                                                    if not bool(n) and bool(a): 
                                                        if isinstance("World",str): 
                                                            if not(True and False): 
                                                                if isinstance(n,(int,float)):
                                                                    if not isinstance(b,list): 
                                                                        return n
                                                                    else: 
                                                                        return a
                                                                else: 
                                                                    return a
                                                            else: 
                                                                return a
                                                            
                                                        else: 
                                                                return a
                                                    else: 
                                                        return a

                





    return n


def n(a:int):
    return a * a


start=perf_counter()
print(start)
try: 
    with ThreadPoolExecutor() as executor: 
        f1 = executor.submit(f)
        f2 = executor.submit(h,1)
        f3 = executor.submit(g)
        f4 = executor.submit(n,a=10)

        f1.result()
        f2.result(5)
        print(f3.result())
        print(f4.result())
except TimeoutError as error: 
    print(f"{error}")
    pass
finally: 
    print("Ok")

s=perf_counter()
f6=Thread(target=h,args=(2,))
f6.start()
f6.join(5)
e=perf_counter()



finish=perf_counter()
print(finish)
total=round(finish - start,2)

print("The total to run: ", total)
print("Total: ", round(e - s,2))

