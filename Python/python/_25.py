from time import (sleep,perf_counter)
from concurrent.futures import (ThreadPoolExecutor, as_completed)
from random import randint
from file_detection import FileManager, python_docx, python_xlsx
from _23_multitreading import learn,Greet
from _22_bank_mangement import col, InitBank
from functions_to_use import simple,compuesto


def download_website (url:str)->str: 
    calculating_time=randint(0,1 )
    short=randint(1,5)
    large=randint(6,10)

    time_required= large if calculating_time else short
    sleep(time_required)

    return f"Finished downloading data from {url}"

 



if __name__ == "__main__": 
    urls:list=[
            "https://api.example.com/data/1",
    "https://api.example.com/data/2",
    "https://api.example.com/data/3",
    "https://api.example.com/data/4",
    "https://api.example.com/data/5",]

    file=FileManager()
    file.withtraceback = False
    nw_f="trying.docx"
    #file.create_word(nw_f)



    g=Greet()
    user=InitBank.initiation(1235)
    user2=InitBank.initiation(1236)

    what=lambda:print("Hello World!")
    run_=False


    start=perf_counter()
    try: 


        with ThreadPoolExecutor() as executor:
            results:list=[executor.submit(download_website,url)for url in urls]
            #f1=executor.submit(file.write_word,nw_f,learn,title="Threading")
            f2=executor.submit(file.write_word,nw_f,col,title="Rows")
            f3=executor.submit(compuesto)
            f4=executor.submit(g.yourfriends,Hersy="The Femboy one", Ashley="The aesthetic one", Craice="The tomboy one",Miseru="The normal one")
            my_dict=f4.result()
            f5=executor.submit(file.write_excel,python_xlsx,"Testing",my_dict)


            
    
            f3=executor.submit(simple)
            f6=executor.submit(user.withdraw_amount,1)


            if f6.result(): 
                f7=executor.submit(user2.deposit,1)
                f7.result()

            f8=executor.submit(file.write_txt,"Learning Tread","I am trying to use threding, :|")
            


            f9=executor.submit(g.greet,"Craice",19)
            f10=executor.submit(what)


            
            for f in as_completed(results): 
                print(f.result())


            ver1=True
            #f2.result()
            f3.result()
            ver3=f5.result()
            f8.result()
            f9.result()
            f10.result()
        

            run_ =True
            print("-"*100)
            print("Run_: ", run_, "Ver1: ",ver1, "Ver3",ver3)
            print("-"*100)

            
            
    except: 
        pass

    #file.write_word(python_docx,learn,title="Threading")
    #file.write_word(python_docx,col,title="Rows")
    #my_dict=g.yourfriends(Hersy="The Femboy one", Ashley="The aesthetic one", Craice="The tomboy one",Miseru="The normal one")
    #file.write_excel(python_xlsx,"Testing",my_dict,True)


    end=perf_counter()

    
    print("Every task have been compled. Time Needed: ", round(end - start, 2), " Seconds")

    nt=""""
    
if __name__ == "__main__": 
    urls:list=[
            "https://api.example.com/data/1",
    "https://api.example.com/data/2",
    "https://api.example.com/data/3",
    "https://api.example.com/data/4",
    "https://api.example.com/data/5",
    "https://api.example.com/data/6",
    "https://api.example.com/data/7",
    "https://api.example.com/data/8",
    "https://api.example.com/data/9",
    "https://api.example.com/data/10",
    "https://api.example.com/data/11",
    "https://api.example.com/data/12",
    "https://api.example.com/data/13",
    "https://api.example.com/data/14",
    "https://api.example.com/data/15"

    ]

    file=FileManager()
    g=Greet()
    user=InitBank.initiation(1235)
    user2=InitBank.initiation(1236)


    start=perf_counter()
    with ThreadPoolExecutor() as executor:
        results:list=[executor.submit(download_website,url)for url in urls]
        f1=executor.submit(file.write_word,python_docx,learn,title="Threading")
        f2=executor.submit(file.write_word,python_docx,learn,title="Rows")
        f3=executor.submit(compuesto)
        f4=executor.submit(g.yourfriends,Hersy="The Femboy one", Ashley="The aesthetic one", Craice="The tomboy one",Miseru="The normal one")
        my_dict=f4.result()
        f5=executor.submit(file.write_excel,python_xlsx,"Testing",my_dict,True)
        f6=executor.submit(user.withdraw_amount,15)

        if f6.result(): 
            f7=executor.submit(user2.borrow_money,30)
            f7.result()

        f8=executor.submit(file.create_txt,"Leraning Tread","I am trying to use threding")


        
        for f in as_completed(results): 
            print(f.result())

        f1.result()
        f2.result()
        f3.result()
        f5.result()
        f8.result()
        


    end=perf_counter()

    print("Every task have been compled. Time Needed: ", round(end - start, 2), " Seconds")
    



    
    
    """

    nt += f"\nEvery task have been compled. Time Needed:  {round(end - start, 2), } Seconds"


    with ThreadPoolExecutor() as ex: 
        f = ex.submit(file.write_word,nw_f,nt, title="This Whole thing took me",font_title=("Arial", 50, True))
        ver2=f.result()


        results2:list=[ex.submit(download_website,url)for url in urls]
        for i in as_completed(results2): 
            print(i.result())




    #file.write_word(python_docx,nt,title="This Whole thing took me",font_title=("Arial", 22, True))
    print("-"*100)
    print("Run_: ", run_, "Ver1: ",ver1,"Ver2: ",ver2, "Ver3",ver3)
    print("-"*100)

    if run_ and ver1 and not ver2 : 

        file.open_file(nw_f)
        file.open_file(python_xlsx)



   
    


