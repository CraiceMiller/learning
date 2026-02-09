from mypython.utils import (quickSortDict,mygroupby,Groupby) #type: ignore
from mypython.files import (FileManager) #type: ignore

mydict = [
    {"name":"hersy", 
     "age":18, 
     "country":"altisora", 
     "student":True,
     "info":{
         "phone":3,
         "details": {
             "height":61.5
         }
     }
    
    },
    {"name":"Ashlye", 
     "age":19, 
     "country":"altisora", 
     "student":False,
     "info":{
         "phone":1,
         "details": {
             "height":49.5
         }
     }
    
    },
    {"name":"Craise", 
     "age":17, 
     "country":"altisora", 
     "student":True,
     "info":{
         "phone":2,
         "details": {
             "height":59.5
         }
     }
    
    },
]

p:str= r"C:\Users\Usuario Pc\Desktop\programming\data\studentsDataBase.json"
data = FileManager().read_json(p,False)



print(quickSortDict(data,"basic","age"))
print()
#print(mygroupby(data,"basic"))
