
students:list=[]
def storage(name:str)->None:
    students.append(name)

def add_studentes(name,age,grade):
    students.append(
        {
            "name":name,
            "age":age,
            "grade":grade
        }
    )

    

print(f"Num students {len(students)}, Students: {students}")

if not all(("","","",False,0,None)):
    print("ok")
else:
    print("no okay")

mlist={"a":1,"b":0,"c":1}
print([x for x in mlist if mlist[x]==1])