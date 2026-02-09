from concurrent.futures import ThreadPoolExecutor, as_completed
import random as r 
import time 


list_=[308, 167, 397, 106, 131, 438, 12, 365, 233, 399, 287, 180, 496, 320, 88, 356, 104, 45, 231, 295, 233,
        433, 458, 286, 319, 268, 364, 94, 180, 104, 67, 207, 395, 284, 491, 325, 388, 196,
          476, 436, 240, 225, 252, 273, 138, 152, 107, 308, 107, 85, 168, 204, 432, 136, 144,
            263, 371, 295, 24, 60, 393, 203, 293, 464, 19, 272, 144, 321, 286, 362, 239, 89, 
            196, 433, 85, 40, 105, 344, 213, 244, 28, 158, 237, 114, 293, 27, 218, 319, 278,
              220, 219, 429, 129, 449, 345, 15, 366, 232, 250, 227]


def mydis(ls,n)->float: 
    time.sleep(2)

    return sum(ls) * n




num=lambda n: round(n/100,2)

dis = [num(r.randint(0,99)) for _ in range(99)]


thstart=time.perf_counter()

with ThreadPoolExecutor() as executor:
    results=[executor.submit(mydis, list_,price) for price in dis ]



thend=time.perf_counter()




lstart=time.perf_counter()
result2=[mydis(list_,p) for p in dis]
lend=time.perf_counter()


print("-"*100)
print("Everything is Done wiht Tread, Time: ", round(thend - thstart,2)," Seconds")
print("Everything is Done wiht Loop, Time: ", round(lend - lstart,2), " Seconds")

 



