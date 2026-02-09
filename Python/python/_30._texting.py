from file_detection import FileManager,python_docx #type: ignore
from time import perf_counter 

text1="""
    Things i lern: 
        x:
            will crate a new file and we can write something too, however, if exist it'll raise an error

        w:
            will create a new file if it does not exist and we can write something too, 
            however, if it is exist it will delete all the privios info

        a: 
            will NOT create a new file,only if it is exist we can write something,
            therefore, it will save all the previous info

        r:
            i dunno \n
    
    """


text2=  """
    \n
    x = will crate a new file and we can write something too, however, if exist it'll raise an error
    w = will create a new file if it does not exist and we can write something too, 
    however, if it is exist it will delete all the privios info
    a= will NOT create a new file,only if it is exist we can write something,
    therefore, it will save all the previous info
    r= this only read the file
    
    """

text3="""
#28/28/2025
defaultdict:
    so every new key i will provided it automally become a list (or the value i provide)
    if i do this

    my_defaultdict=defaultdict(set)
    my_defaultdict[key].add(value)

    It is the same to type:
    my_dict={}
    but this do not raise a key error, instead it will create a new key using this value i provided

Sorted: 
    so what i am doing here:

    sorted(people, key=lambda person: person["age"])
    
    In short, key needs a rule to apply to each item, not the result of that rule on a single, non-existent item.
    im telling that i want the new list sorted by the key age of each dict, right?
"""

text4="""
1. NEVER USE THREADDING WITH TWO SAME FILES AT THE SAME TIME. BECUSE IT WILL CORRUPTED IT
2. The file has weight, if the has zero (0) bytes, it will cuz an error. This means the file is 
empty

"""

text5="""
#21/06/2025
HOW TO WRITE BETTER FUNTIONS (by indently.io_):
    1. Write short and concise 
        Examples:
        - get_number
        - display_number
    
    2. Specify a return type 
        Example:
        -> None
        -> str
        -> int

    3. Make as simple and reusable as possible 
        Example:
        A function that only do one single task

    4. Document all your functions: 
        Example: 
        Write the core purpose of the funtion, what it does, what paremeter takes
        what it returns, an example.
        >>> get_number()
            output: 2

    5. Handles the errors appropriately:
        Example:
        raise ValueError
        raise TypeError
    

"""

text6="""
#22/08/2025
I wanna update a json file.
and i get structured: 
    1. First read the json file: 
        with open("my json.json","r") as file: 
            data=json.load(file)
    2. get the specific dict i want. The conclusion i reach was through i binary search :

        def my_dict_binary(dictionaries:list[dict[str,Any]],
                   key:str,
                   target:str)->int: 

            try: 
                start:int=0
                end:int=len(dictionaries)-1

                while start <= end:
                    mid:int= (start + end) // 2

                    middle_value = dictionaries[mid][key]
                    
                    if middle_value == target: return mid

                    if middle_value < target: start = mid +1

                    else: end = mid -1


                return -1

            except: 
                return -1

                
    data.sort(key=lambda d: d["Name"])
    index=my_dict_binary(data,"Name","Hersy") #2 i guess 

    3. Acces the specific key and 4. update the value
    data[index]["Country"] = "japan"

    5. save againthe json file: 
        with open("my json.json","w") as file: 
            json.dump(data,file,indent=4)


BUT I DUNNO IF THIS IS THE CORRECT APROACH. But please dont give the answer i wanna 
discover it by myself, just guide me please
        





"""

text7="""
MODULE:
    This Module provided all the necesary to work with file in the current 
    computer. This module provided FileManager class. Where you can create, 
    read and write simple thing in file like: 
        - word files (.docx)
        -excel files (.xlsx)
        - json files (.json)
        -text files  (.txt)

    Also give provided a biniary search to look all the iterable in a effiency way

UPDATES:
    16/08/2025
    20/08/2025
    25/08/2025
    


"""

text77="""
#26/08/2025
f1= th.Tread()
    target: is the main purspose of the object, this is the funition we want to run 
    args: This must be a tuple of positional arguments fo the funtion we provide early 
    kwargs: This must be Mapping (a dictionary i guess). This will pass the key as the 
    keyargument and the value as the value of the parameter. 

        We cannot write args and kwargs if the funtion doesnt need. 
            >>> def greet()->None: 
                    ...

    the parameter args is useful if we have funtion that have positional arguments only: 
            >>> def greet(name,age,/)->None: 
                    ...

    Likewise we use the parameter kwargs if we have a funtion that have key arguments only
            >>> def greet(*,name,age)->None: 

    Moreover we can use both (args and kwargs ) when the funtion has position and key argumentes 
            >>> def greet(name,*,age,city,language)->None: 

We use the .start() method to indeed run the funtion. 
f1.start()

Nevertheless I have Three questions: 
    if the funtion return a value, where is it stored ?
        >>> def gree(name,age,/)->str: 

    And What is the differente between run and start method 
    I Dont got it what timeout means neither .join() metods

"""



text8="""
----------------------------------------
       |COLUMN 0 | COLUMN 1 | COLUMN 2 |
----------------------------------------
ROW 0 |
----------------------------------------
ROW 1 |
----------------------------------------
ROW 2 |
----------------------------------------


n=top
s: botton
w:left
e: right

{
        "user": "mysafetyplace.54@gmail.com",
        "password": "you//don'Tn33d1T",
        "balance": 702.77,
        "wallet": 285,
        "username": "Craice Miler",
        "debt": 0
},


"""

text9="""
my_dict={
    "a":[1,2,2,5,5,6,7,8,10,70.40,20,10],
    "b":["a","b","c",""],
    "c":[90.50,10,20,0],
    "d":["",0,[],0,""]
}

for index, item in enumerate(zip(*my_dict.values())):
    print()
    print(index,f"{item}")

print()
print(list(zip(my_dict.values())))
print(list(zip(*my_dict.values())))
print()

"""

text10= """
Firt what the f*** this works: 
    leftSide:list=mergeSort(iterable_[:middle])
    rightSide:list=mergeSort(iterable_[middle:])
i know this is call recursion, but why it works, i mean, when i call this one:
mergeSort(value)
it automally call others two mergeSort function. so why i dont get a Recurtion error?
since this will always be calling each other: 
how i see it: 
     if i call it once. leftSide will call it again, inside this another call, lefiSide will it 
     again. for me this will call it over and over again . 


second question: 
how this even posible: 
i=j=k=0

third question: 
why i need to do three loops

four question: 
why am i so stupid that i can solve this problem for myself and i needed help to do it?



"""

text11="""
#addinf more data in a existing file 
df = pd.read_excel("Sale_Management.xlsx")


new_product4 = {
    'Product_ID': ['P115'],
    'Product_Name': ['MousePad'],
    'Category': ['Accessories'],
    'Price_USD': [60.50],
    'Quantity_Sold': [25],
    'In_Stock': [True],
    'Rating': [8]
}

new_row_df4= pd.DataFrame(new_product4)

df = pd.concat([df, new_row_df4], ignore_index=True)
df['Total_Revenue'] = df['Price_USD'] * df['Quantity_Sold']

try: 
    with pd.ExcelWriter("Sale_Management.xlsx", engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        df.to_excel(writer, sheet_name='Products', index=False)

except FileNotFoundError as e:
    print(e)
except PermissionError as e:
    print(e)
except ValueError as e :
    print(e)
"""

text12="""
#29/08/2025
__hash__ method only declare the class itself as a Hashable.
all classes are hashables... Nonetheless, it the class has the __eq__ method, 
the class is not hashable anymore, untill you write the __hash__ method manually

__getitme__ method only help to use square bracket to acess a value within the class

__iter__ method only convert a value in the class in a Iterator (list)

"""

text13="""
MY CONCLUTIONS: 
    -So, the abstractmethod tell us that every class based of the class that 
    have a abstractmethod,it MUST have their own method, It'll raise an TypeError otherwise

    - if we dont write the abstractmethod, it will only add more info base of the previous one..

    -ABC enforce the class that the others classes have the requeried method.
    if we dont type ABC, python will ignore the @abstractmethod and it won't raise a TypeErorr,
    Therefore it is a useful tool that ensure the developer write the method needed of each 
    subclases (childclasses)
        i this one like the english grammar. We use 'must' to tell people important things (it is 
        mandatory). We use 'should' to tell people advice (it could be done or not)

        The same applies here, we use ABC and @abstractmethod to tell 'must', 'should 'otherwise

    -Pizza class works due it child of Circle and circle has the area method, therefore, Pizza
    inheritance everything from Circle class

    -In my Dimon class, in the method name(), it won't raise a TypeErrorr because it is not a 
    abstractmethod...

"""



content:dict[str,str]={
    "Learing the method Open()":text1 + text2,
    "Learning defaultdict()": text3, 
    "Advise for me >:v": text4,
    "HOW TO WRITE BETTER FUNTIONS":text5,
    "Updating a json file": text6,
    "My module file": text7,
    "Learnig Thread:": text77,
    "How to work .grid() in customtkinter":text8,
    "A simple funtion ": text9,
    "Merge algorithm": text10,
    "Learning Pandas": text11
}

start=perf_counter()
file=FileManager()
print(file.word_styles(python_docx))

should_open:list=[]

for title,txt in content.items(): 
    verification:bool=file.write_word(python_docx,
                                      txt,
                                      title=title,
                                      heading= "Heading 2",
                                      font_title=("Arial", 18, True)
                                      )
    should_open.append(verification)


if all(should_open):
    file.open_file(python_docx)
else: 
    print("somethig goes wrong")






end=perf_counter()
final=perf_counter()
print("Time need : ", round(final,2))


