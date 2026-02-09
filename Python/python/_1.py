
Currency_:dict={"quetzales":7.68,"mexican pesos":18.54,"colombian pesos":4108.25,"peruvian soles":3.53,"yen":147.72,"brazilian reais":5.56,"euro":0.85}

def currency_to_dollars(currency:str,
                        amount:int|float)->int|float:
    if not currency in Currency_:
        print("sorry, but we don't have that value")
        return amount
    
    dollars=  amount / Currency_[currency] 

    return round(dollars,2)

def dollars_to_currency(currency:str,
                        dollars:int|float)->int|float:
    if not currency in Currency_:
        print("sorry, but we don't have that value")
        return dollars
    
    currency_change=   Currency_[currency] * dollars

    return round(currency_change,2)





def evaluating_passing_students(course:dict[str,int|float],
                                approved_note:int=60
                                )->list[str]:
    """\nDescription: 
    \nThis only will return a list of students who passed a certain note..."""
    passing_students:list=[]
    for key,value in course.items():
        if value > approved_note:
            passing_students.append(key)
 
    return passing_students

list_of_student:list=['hersy','craice','ashley','stephany', 'mayra','michelle','edurado','grelinda']

list_of_courses:dict={
    'math':{'hersy':50,'craice':80,'ashley':60,'stephany':74, 
            'mayra':45,'michelle':65,'edurado':70,'grelinda':30},
    'computer scince':{'hersy':89,'craice':79,'ashley':70,'stephany':80, 
            'mayra':60,'michelle':84,'edurado':90,'grelinda':50},
    'art':{'hersy':92,'craice':50,'ashley':75,'stephany':45, 
            'mayra':80,'michelle':62,'edurado':75,'grelinda':100},
}
for key,value in list_of_courses.items():
    print("Passing students of {}".format(key))
    students:list=evaluating_passing_students(value)
    for index, names in enumerate(students,1):
        print(f"{index}. {names.capitalize()}")
    print("\n")

