#31/082025

from time import perf_counter
ms=perf_counter()


from mypython.dictionary import CreateDictForPandas #type: ignore
from mypython.file_detection import FileManager,python_xlsx #type: ignore
from my_original_character import craice,hersy,ashley #type: ignore
from functools import wraps
from concurrent.futures import ThreadPoolExecutor,as_completed
import mypython as my #type: ignore
me=perf_counter()

file=FileManager()

def mytime(function):

    @wraps(function)
    def mywrap(*args,**kwargs):
        s=perf_counter()

        result=function(*args,**kwargs)

        e=perf_counter()
        final=e-s
        print(f"Time needed for the funtion {function.__name__} : {final:.4f} Seconds ")
        print()
        return result 
    
    return mywrap
    


@mytime
def greet():
    print("hello world!")






@mytime
def main1()->None: 
    my_dict=CreateDictForPandas().convert(craice).length().show
    my_dict2=CreateDictForPandas().convert(hersy).length().show
    my_dict3=CreateDictForPandas().convert(ashley).length().show
    global file

   


    for i in my_dict.values(): 
        print()
        print()
        print("Lenght: ", len(i))
        print("Value: ")
        print(i)



    f1=file.write_excel(python_xlsx,"Data",my_dict)
    f2=file.write_excel(python_xlsx,"Data",my_dict2)
    f3=file.write_excel(python_xlsx,"Data",my_dict3)


    if all((f1,f2,f3)):
        file.open_file(python_xlsx)
    else: 
        print("No okay ....")


@mytime
def main2()->None: 
    global file
    df = file.read_excel(python_xlsx,"Data")
    print(df.columns)


@mytime
def counter()->int:
    for i in range(1000): 
        if i ==970: 
            return i
        
    return 0

from time import sleep
@mytime
def meet(name:str): 
    sleep(4)
    return f"Hello {name}, Nice to meet you :)"





if __name__ == "__main__": 
    x=perf_counter()
    with ThreadPoolExecutor() as executor: 
        executor.submit(main2)
        f=executor.submit(counter)
        f2=[executor.submit(meet,x) for x in ["Ashely","crace","Hersy"]]
        f3=executor.submit(counter)



        print(f.result())
        print(f3.result())
        for i in as_completed(f2): 
            print(i.result())

    y=perf_counter()
    mf=me-ms
    final=y-x
    print(f"All task done in {final:.2f}s")
    print(f"All modules done in {mf:.2f}s")
    help(my)



        
    

    
    




