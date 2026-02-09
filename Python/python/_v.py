from typing import Any
from _collections_abc import Iterable
from time import sleep

class ManagementPizaaShop:
    BALANCE:float|int=1132000.50

    People_Attender:int=17525

    PIZZA_NAME:str="Little Hungry Bear"




class kitchenPizza: 


    Ingredients:dict[str,int|float]={
        "Pepperoni":2,
        "Mushrooms":2.5,
        "Onion": 0.5,
        "Tomatoes": 2.80,
        "Green peppers":1.90,
        "Ham":2.50,
        "Cheese": 5.25,
        "Dough":0.90,
        "Sauce":0.60
    }

    Production_Cost:dict[str,int]={
        "Large":8,
        "Medium":5,
        "Small":3
    }


    Tax_rate:float=0.09


    def __init__(self) -> None:
        self.chart:dict={}
        
    @staticmethod
    def extra_pizza_calutalator(_ingredients_wanted:list)->float|int:
        """
        \nDescription: 
        \nA funtion that caltulate the value of a pizza 
        according to ingredients given 
        """
        total:int|float=0
        global Ingredients

        selection_ingredients_given:list=list(filter(lambda ingredintes: ingredintes in kitchenPizza.Ingredients,_ingredients_wanted))

        for item in selection_ingredients_given:
            total += kitchenPizza.Ingredients[item]

        
        return total


    def get_price_pizza(self, _quantity:int,_size:str, _extra_cost:list)->float|int:
        
        #this variable will get the price cost base on the size 
        prepared_cost:int=kitchenPizza.Production_Cost[_size]
        #this will get the price of the extra ingredintes only if there is 
        extra_cost:int|float=self.extra_pizza_calutalator(_extra_cost) 
        #this wil get the tax of the amount 
        taxes:int|float=((prepared_cost + extra_cost) * kitchenPizza.Tax_rate)

        #this is the total of the pizza 
        total:int|float=round((prepared_cost + extra_cost + taxes) * _quantity,2)
        return total


        

    def cheese_pizza(self,
                     _quantity:int,
                    _size:str="Medium")->None:
        #this is the total of the pizza 
        total:int|float=self.get_price_pizza(_quantity,_size,["Cheese","Dough","Sauce"])

        #this will add the orded into the chart
        self.chart["Cheese Pizza"]=(_size,_quantity,total)
    
    def ham_pizza(self,
                     _quantity:int,
                    _size:str="Medium")->None:
        #this is the total of the pizza 
        total:int|float=self.get_price_pizza(_quantity,_size,["Ham","Dough","Dough","Sauce"])

        #this will add the orded into the chart
        self.chart["Ham Pizza"]=(_size,_quantity,total)

    
    def personality_pizza(self,
                        _quantity:int,
                        more_ingredients:list,
                        _size:str="Medium")->None:
        """
        \nDescription: 
        \nThis funtion will only get total cost of the pizza 
        
        """
        ingredient_:list=["Dough","Sauce"]
        ingredient_.extend(more_ingredients)

        #this is the total of the pizza 
        total:int|float=self.get_price_pizza(_quantity,_size,ingredient_)

        #this will add the orded into the chart
        self.chart["Personality Pizza"]=(_size,_quantity,total)


class PizzaShop(kitchenPizza,ManagementPizaaShop):
    def __init__(self,
                 name:str="User",
                 money:int|float=0,
                 bag:dict|None=None) -> None:
        super().__init__()
        self._name=name
        self._money=money
        self._bag=bag

        self._total:int|float=0

        ManagementPizaaShop.People_Attender +=1
        print(f"Hello {self._name}. Welcome to {ManagementPizaaShop.PIZZA_NAME} " + "-"*50)


    def list_total(self)->None:
        for key , values in self.chart.items():
            print(f"{values[1]}|{values[0]}{key}${values[2]:.>25} ")
            self._total += values[2]


    def pay_bill(self)->dict:
        print("Your pizza will cost ${}".format(self._total))
        sleep(4)
        if  self._money < self._total:
            print("it seems you don't have enough money to pay with ")
            my_dict:dict={"Message": "you don't get anyting"}

            if self._bag is not None:
                self._bag.update(my_dict)
                return self._bag
            

            return my_dict

        else:
            self._money -= self._total
            ManagementPizaaShop.BALANCE += self._total

            self._total=0
            print("Here you go, enjoy it...")

            if self._bag is not None:
                self._bag.update(self.chart)
                return self._bag

            return self.chart

    




    @classmethod
    def selecting_size(cls)->str:
        for index,items in enumerate(cls.Production_Cost.keys(),1):
            print(f"{index}. {items}")

        chose=None
        while chose not in cls.Production_Cost.keys():
            chose=input("Select a size: ").capitalize()
        
        return chose

    @staticmethod
    def selecting_quantity()->int:
        while True: 
            try:
                quantity:str|int=input("How many do you going to buy?: ")
                quantity2:int= int(quantity)
                return quantity2
            except ValueError :
                continue

    @classmethod
    def selecting_more_ingredints(cls)->list:
        more_ingredints:list=[]
        already_chosen:set=set()

        for index, items in enumerate(cls.Ingredients.keys(),1):
            print(f"{index}. {items}")

        chose=None
        while chose !="Q":
            chose=input("Select the ingredints you want(press 'q' to quit): ").capitalize()
            if chose in already_chosen:
                print("You already chose that")
                continue 
            already_chosen.add(chose)
            more_ingredints.append(chose)
        
        return more_ingredints



    def ordering_pizza(self)->None:
        while True:
            print("1.Cheese Pizza ")
            print("2.Ham Pizza ")
            print("3.Personality Pizza ")
            print("4.Exit ")
        
            chose=input("What do you going to order today: ")

            match chose: 
                case "1":
                    size:str=self.selecting_size()
                    quantity:int=self.selecting_quantity()
                    self.cheese_pizza(_quantity=quantity,
                                      _size=size)

                case "2":
                    size2:str=self.selecting_size()
                    quantity2:int=self.selecting_quantity()
                    self.ham_pizza(_quantity=quantity2,
                                      _size=size2)

                case "3": 
                    size3:str=self.selecting_size()
                    quantity3:int=self.selecting_quantity()
                    more_ingredient:list=self.selecting_more_ingredints()

                    self.personality_pizza(_quantity=quantity3,
                                           more_ingredients=more_ingredient,
                                           _size=size3)

                  
                case "4":
                    break
                case _:
                    print("Select a valid option dear {}".format(self._name.capitalize()))

        



def main()->None:
    name:str="Craice"
    money:int|float=590.45



    print(f"{name} went at {ManagementPizaaShop.PIZZA_NAME}")
    print(f"They have in money {money}")

    User1=PizzaShop(name,money)
    print()
    User1.ordering_pizza()
    print()
    User1.list_total()
    print()
    bag=User1.pay_bill()
    print()

    print(f"{name} went at {ManagementPizaaShop.PIZZA_NAME}")
    print(f"They have in money {money}")

    print("and they got:")
    for key,value in bag.items():
        print(f"{value[1]} {key} {value[0]}")



if __name__ == "__main__":
    main()


