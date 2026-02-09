from functions_to_use import dollars_to_currency, currency_to_dollars
from dataclasses import dataclass,field
from typing import ClassVar,Any, Iterable



@dataclass(order=True, slots=True)
class DataUser:
    """
    DESCRIPTION:
        I think
    """

    _username:str
    _password:str
    _is_member:bool=field(init=False,default=True)

    _num_user:ClassVar[int]=0

 

class User(DataUser):
    def __init__(self,_username,_password,d:Any=2,e:Any="None") -> None:
        super().__init__(_username,_password)
        self.d=d
        self.e=e

  
    """
    DESCRIPTION:
        I think
    """

    def display_info(self)->None:
        print(f"{self._username} | {self._password}")

class A:
    def __init__(self,a,b,c) -> None:
        self.a=a
        self.b=b
        self.c=c

class B(A):
    def __init__(self, a, b, c,d,e) -> None:
        super().__init__(a, b, c)
        self.d=d
        self.e=e



def get_discount(prices: Iterable[float],
                 percent: float
                 )->float:
    """
    DESCRIPTION:
        A function that calculate the total of the sum of prices in the provided list and 
        applies a discount based on the given discount rate. If the discount is invalid (eg., 
        negative or greater than 1), the funtion raise a ValueError.

    RETURN:     
        (a float object) The total of the price later to apply the discount

    EXAMPLE: 
        >>> get_discount({2,32,50,86},0.25)
        output: 127.5
    
    """
    
    if not ( 0 <= percent <= 1):
        raise ValueError(f"Invalid discount rate: {percent}. Must be between 0 and 1")
    
    if  not all(isinstance(price, (int,float)) and price >= 0 for price in prices):
        raise ValueError("All prices must be non-negative numbers")
    
    total: float = sum(prices)

    return total * (1-percent)


def main()->None:
    dollar=currency_to_dollars("won",11_000_000)
    quetzales=dollars_to_currency("quetzales",dollar)
    print(dollar)
    print(F"Total cost: Q{quetzales:,}")




    user1=User("hersyhelston@gmail.com","Hersy_Helson.123",3)
    user1.display_info()
    print(user1)

    user2=User("none","none")
    a=B(1,2,3,4,5)

    c=get_discount({2,32,50,86},0.5)
    print(c)


 




if __name__ == "__main__":
    main()
