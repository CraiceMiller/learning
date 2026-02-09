from file_detection import FileManager,python_docx #type: ignore
from functions_to_use import mygroupby,get_most_common_dict  #type: ignore
from time import perf_counter 
type_="Type"
reason=".docx"

path=r"C:\Users\Usuario Pc\Desktop\Learning_Python\Historial file.json"


s=perf_counter()
f=FileManager()


my_list:list[dict]=[
    {
        "name": "Hersy",
        "age":18
    },
    {
        "name": "Craice",
        "age":19
    },
    {
        "name": "Ashley",
        "age":17
    },
    {
        "name": "Misery",
        "age":18
    },
        {
        "name": "Sthepany",
        "age":17
    },
        {
        "name": "Craice",
        "age":19
    },
    {
        "name": "Ashley",
        "age":17
    },
            {
        "name": "Craice",
        "age":19
    },
    {
        "name": "Mark",
        "age":20
    },
    {
        "name": "Anthony",
        "age":21
    },
]





info=f.read_json(path,False)
my_dict=mygroupby(info,type_)

fd=f.read_json(path,True)


print(my_dict.keys())
top=get_most_common_dict(my_dict[reason],"Day")

print(f"The json file has {len(top)} objects here...")
print(top)
print(get_most_common_dict(my_list,"name"))
print()
print(fd.head())
print()
print(str(fd.tail()))
print()
print(fd.columns)

save=f.write_word(python_docx,str(fd.tail()), title="Pandas in a Json File",font_title=  ("Arial", 25, True))           
   

en=perf_counter()
final=en - s

print()
print()
print("Time needed: ", round(final,2))


if save: 
    f.open_file(python_docx)
else: 
    print("Dont :( ")