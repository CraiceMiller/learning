
from file_detection import FileManager,python_docx,python_xlsx #type: ignore
from bank import Bank #type:ignore
from my_ocs import hersy, craice,ashley #type:ignore





if __name__ == "__main__": 
    file=FileManager()
    my_dict:dict={
        "Names":["Alison","Sthephany","Endriew","Craice"],
        "Ages": [18,17,19,18],
        "Lenguage": ["Spanish","English","Japanes","English"],
        "Country": ["Altisora"]*4,
    }

    historial="Historial file.json"
    bank="User Accounts.json"


   
    
    acount1=craice.get("bank")
    acount2=hersy.get("bank")
    acount3=ashley.get("bank")

    #file.write_json(bank,acount1)
    #file.write_json(bank,acount2)
    file.write_json(bank,acount3)



    
    

   
 
 


    





    """   
    def greet()->None:
        print("Nice to meet you {}")


    @greet()
    def hello()->None: 
        print("Hello {}")


    """
   
   


 
   
    #x=file.create_word(name,"Such a loser")
    #file.create_txt("I dunno.txt")
    #file.read_txt("I dunno.txt")

    #path=file.path_downloads("Index.docx")
    #title="Learning Python Every Day"
    #text="Today (20/08/2025) i learn how to use new fetures in Document()"

    #file.write_word(python_docx,text,title=title,table_maker=my_dict)

   

   
  

    









    
    

    
    
   


   
   





 
   






