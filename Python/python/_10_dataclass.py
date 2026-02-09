#2/8/2025
from dataclasses import dataclass, field
from typing import ClassVar
import inspect
"""
frozen only does that all the values we give it,will never change (inmutable)
kw_only,this is just tell us that all the new classes object MUST have the arguments keywords
"""
class BookManually:
    #creating class instances 
    total_books:int=0

    #Creating dunder methods
    def __init__(self,
                 title:str,
                 gender:str,
                 relese:int,
                 type:str="book") -> None:
        #creating the instances 
        self._title = title 
        self._gender=gender
        self._release_year=relese
        self._type=type
        #creaing other instnaces 
        self._is_available:bool=True
        self._description:str="Indeed, it is a book"
        #add a new book into the total_books
        BookManually.total_books +=1

    
    def __str__(self) -> str:
        return f"Title: {self._title}. Type: {self._type}"
    
    def __eq__(self, __value: object) -> bool:
        return self.__dict__ == __value.__dict__
    
    def __repr__(self) -> str:
        return "{},title={},gender={}".format(self.__class__.__name__, self._title, self._gender)

    #creating methods 
    def read(self)->None:
        print(f"Reading {self._title}")
    
    def add_year(self)->None:
        print(f"Old year: {self._release_year}")
        self._release_year += 1
        print(f"Current year: {self._release_year}")

    #creating a class method
    @classmethod
    def count_books(cls)->None:
        print(f"There are {cls.total_books} here")
        


@dataclass(order=True,kw_only=True,slots=True,unsafe_hash=True)
class Book:
    #1. creating the instances
    #dataclass creat autmally the __init__ method, and we onlly need to the the instances
    _title:str
    _gender:str
    _release_year:int
    _type:str="book"
    #Is it the same to do what i write in BookManually

    #2. creating the classes instances 
    total_books:ClassVar[int] =0

    #3. Creating more instances
    _is_available:bool=field(init=False, default=True)
    _description:str=field(init=False, default="Indeed, it is a book")

    
    #4. Creating the dunder method i want, instead of a bunch of them 
    def __str__(self) -> str:
        return f"Title: {self._title}. Type: {self._type}"
    
    #5. creating a method
    def read(self)->None:
        print(f"Reading {self._title}")
    
    def add_year(self)->None:
        print(f"Old year: {self._release_year}")
        self._release_year += 1
        print(f"Current year: {self._release_year}")
    
    #6. creating a class method
    @classmethod
    def count_books(cls)->None:
        print(f"There are {cls.total_books} here")

    #7. tracking amount of books
    def __post_init__(self)->None:
        Book.total_books += 1


#since dataclass primary purpose is to storage data, can i creat just a separate class?
@dataclass(order=True,kw_only=True)
class Data:
    _title:str
    _gender:str
    _release_year:int
    _type:str="book"


    total_books:ClassVar[int] =0


    _is_available:bool=field(init=False, default=True)
    _description:str=field(init=False, default="Indeed, it is a book")


    def __str__(self) -> str:
        return f"Title: {self._title}. Type: {self._type}"
    
    
 

#and create another taht will goes all the logical and everymethods i want to?
class Book(Data):
    def read(self)->None:
        print(f"Reading {self._title}")
    
    def add_year(self)->None:
        print(f"Old year: {self._release_year}")
        self._release_year += 1
        print(f"Current year: {self._release_year}")
    

    @classmethod
    def count_books(cls)->None:
        print(f"There are {cls.total_books} here")

    def __post_init__(self)->None:
        Book.total_books += 1

#yes





"""
PROS:
    1. It avoid us to write the repetitives dunder methods (__repr__,__int__,__eq__, so on)
    2. It save us a lot of time, for instance,if we wanna to change one thing, it will change 
    the whole class automatly

DISADVENTAGES:
    1. IF the class it's frozen we cannot modify anything

"""

info: dict = {
    "title":"MY Hero Academia",
    "gender": "Shonen",
    "published": 2014,
    "type": "manga"
}

   


def main()->None:
    #CREATING THE CLASSES METHODS
    manga:Book=Book(_title= "I love your cruddy",
                    _gender="Yuri",
                    _release_year=2021,
                    _type= "Manga")
    
    comic:Book=Book(_title= "Hilda and the troll",
                    _gender="Children novel",
                    _release_year=2010,
                    _type= "Comic")
    
    manga_2:Book=Book(_title = info["title"],
                      _gender=info["gender"],
                      _release_year=info["published"],
                      _type=info["type"])
    
    manga_3:Book=Book(_title= "I love your cruddy",
                    _gender="Yuri",
                    _release_year=2021,
                    _type= "Manga")

    
    manga_4:BookManually=BookManually("Dangaronpa","mistery",2010,"manga")
    book:BookManually=BookManually("Japanese Dictionary","educative",2000,"dictionary")
    manga_5:BookManually=BookManually("Dangaronpa","mistery",2010,"manga")
    
    #book:Book=Book("Japanese Dictionary","educative",2000) # i cannot do this due 'kw_only'
    

    #TESTING MY OWN CONCLUSION
    print(inspect.getmembers(Book,inspect.isfunction))
    print()
    print(manga.__repr__())
    print(manga.__str__())
    print()
    
    #manga._title="Re: Zero", #i cannot do this due the 'frozen' keyword in dataclass
    print(comic < manga) # i Can do this due 'order' keyword in dataclass
    print(manga)
    print(repr(manga))
    print(manga_2)
    print(manga == manga_2)
    print(manga == manga_3)
    comic.read()
    manga.count_books()
    comic.add_year()

    #BookManually
    print(manga_4)
    print(repr(manga_4))
    print(manga_4 == book)
    print(manga_4==manga_5)
    manga_4.count_books()
    book.read()
    book.add_year()




if __name__ == "__main__":
    main()