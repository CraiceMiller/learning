from mypython.file_detection import FileManager,my_dict_binary #type: ignore
from mypython.bank import BankOunt #type: ignore
from mypython.dictionary import CreateDictForPandas #type: ignore
from mypython.watch import MyWatch #type: ignore
from dataclasses import dataclass
from typing import ClassVar,Self,Mapping
from time import sleep
from collections import defaultdict






@dataclass
class InventaryStore:
    """
    This is where Every product will be storage...

    This class will only storage every product as a dict within a list...

    update: 
    04/09/2025
    
    """

    STOCKS:ClassVar[str]=r"C:\Users\Usuario Pc\Desktop\Learning_Python\whatever\My_Classes\Plushy Store Inventary.json"
    DATA:ClassVar[str]=r"C:\Users\Usuario Pc\Desktop\Learning_Python\whatever\My_Classes\Inventary.xlsx"
    sales:ClassVar[str]="Sales"
    customers:ClassVar[str]="Customers"
    ITEMS_STORAGES:ClassVar[list[dict]]=FileManager().read_json(STOCKS,False)
    STOREBANKACCOUNT:ClassVar[BankOunt]=BankOunt.initiation(1237)




    @classmethod
    def display_inventary(cls)->None:
        """
        THIS ONLY CREATE A DETAIL LIST OF EVERY PRODUCT IN THE INVENTARY    
        """
        print('-'*40 +  'PRODUCTS STORAGE IN THE INVENTARY'+ '-'*40)
        for index, products in enumerate(cls.ITEMS_STORAGES,1):
            print('-'*40 + f"{index}. Product {products.get('product')}" + '-'*40)
            for key, value in products.items():
                if (key=='extra_characteristics'):
                    print('-'*30+ 'Extra Information'+ '-'*30)
                    for extra,info in value.items():
                        print(f"{extra}: {info}" )
                else:
                    print(f"{key}: {value}")
            if products.get("extra_characteristics") is None:
                print("This product doesn't have any extra details  ")
                    

            print()
                
           
    @classmethod
    def display_quantity_product(cls)-> None:
        print(f"Curretly we have {len(cls.ITEMS_STORAGES)} differents products")
       
    
    @classmethod
    def add_more_stock_existing_product(cls,
                                        product_name:str,
                                        more_stock:int
                                        )->None:
        """
        Description:
        This method will create more stock to an specif existing product. Rasie ValueErrro if more_stock
        is not a interger
        """
        if not isinstance(more_stock,int): raise ValueError("The stcoks must be an interger")

        #SEraching the product
        index=my_dict_binary(cls.ITEMS_STORAGES,"product",product_name)
        if  index == -1:
            print('Product not found!!','product')
            return 
        

        #Accesign the specific dict
        data=cls.ITEMS_STORAGES[index]
        print(f"Old stock: {data["stock"]}")



        #UPDATING THE DATA
        data["stock"]  += more_stock
        FileManager().update_json(filePath=cls.STOCKS,
                                      search_key="id",
                                      search_value=data["id"],
                                      **data)


       
        print(f"Currently stocks: {data["stock"]}")
        print(f"The stock of '{data['product']}' has uppdate successfully ")
        

    @classmethod
    def add_new_products(cls,
                    product:str,
                   price:float,
                   stocks:int,
                   **extra_info)->None: 
        """
        this methos will only add new  products to the Store's Inventary...
        """
        
        if my_dict_binary(sorted(cls.ITEMS_STORAGES,key=lambda p:p["product"]),"product",product) != -1: 
            print(f"{product} already exist")

            return 


        if extra_info:
            adding_new_product:dict= {
            "id":max([n["id"] for n in   cls.ITEMS_STORAGES]) +1,
            "product": product,
            "price": price,
            "stock": stocks,
            "extra_characteristics":extra_info
            }

        else : 
            adding_new_product:dict= { #type: ignore
            "id":max([n["id"] for n in   cls.ITEMS_STORAGES]) +1,
            "product": product,
            "price": price,
            "stock": stocks
            }

        if FileManager().write_json(cls.STOCKS,adding_new_product): 
            print("The new product was succesfully added")
        


     
#this is where i sell all my stuff 
class PlushieStore(InventaryStore):
    def __init__(self,
                 financing:BankOunt,
                 name:str="User"
                 ) -> None:
        
        """
        PARAMETERS: 
            _name: it will storage the name of the customer. 
            self._financing: it will handle all the money logic based of my previous proyect 'BankOunt'
            self._bag: it dunno why i write this 

            slef._chart: it is a defaultdict to storage all the tproducts. The  key is string,
              meaning the product to buy and the value is a list where the first value is the 
              stocks to buy and the second value is the price of the product

            self._total: The final amount of the customer purchase
            self.is_packing: track if the chart is ready to pack

        
        """
        
        self._name:str=name
        self._financing=financing



        self._chart:defaultdict=defaultdict(lambda:[0,0])
        #the chart is a string key, meaning the product to by and the value meaning the stocks to buy
        self._total:float = 0
        self.is_packaging:bool=False
        self._products_selling=[p.get('product') for p in self.ITEMS_STORAGES]
        self._prices_selling=[price.get('price') for price in self.ITEMS_STORAGES]
        self._stocks_selling=[stock.get('stock') for stock in self.ITEMS_STORAGES]
        self._checkerleft:int=3


    def savepurchaseinfo(self,description:str="")->None:
        if not self.is_packaging: 
            print("There are no any purchase right now")
            return 


    
        
        for product,info in self._chart.items():
            data=CreateDictForPandas().setvalues(
                ["Date","Customer","Product", "Quantity","Price", "Total", "Description" ],
                MyWatch.get_local_time(),self._name,product,info[0],info[1], (info[0]*info[1]),description
            )

            if FileManager().write_excel(self.DATA,self.sales,data.show): 
                print("The Data was succesfully save") 


        

    def display_products_to_sell(self)->None:
        """
        Description: 
        Display the list of every product and stocks avaliby in the Store's inventary
        """
        
        
        print("\nItems to sell".title())
        
        for num,(key,values,stock) in enumerate(zip(self._products_selling, self._prices_selling,self._stocks_selling),1):
                print(f"{num}.{stock:<5}| {key:.<40}${values}")
           
    def display_chart(self)->None: 
        """
        Display the chart that the customer pick. it'll print 'The chart is currently empty'
        if the customer did not pick anything...
        
        """
        if not self._chart:
            print("The chart is currently empty")
            return 
        
        print("Your current chart", "."*80)
        print(f"{"quantity":<10}|{"product":<10}")
        for product,quantity in self._chart.items(): 
            print(f"{quantity[0]:<10}|{product}")

        print(f"Total of the purchase will be ${self._total:,.2f}")

        print()


    def selecting_stuff(self,chose:str,quantity:int)->bool:
        """
        Desciption:
        Search of all the data to find the target product.
        Therefore, the customer must to type it correctly
        Moreover, it will storage into the self._chart parameter

        Return : 
            False if the item was not found; if there are no stocks lef
            True otherwise, meaning the itemas was save succesfully
    
        """

        
        try: 
            index=my_dict_binary(sorted(self.ITEMS_STORAGES,key=lambda p:p["product"]),"product",chose)

            if index == -1: 
                print("select a valid item")
                return False


            if (self._chart[chose][0] > self.ITEMS_STORAGES[index]["stock"]) or \
                (self.ITEMS_STORAGES[index]["stock"] <=0) or \
                ( self.ITEMS_STORAGES[index]["stock"] - self._chart[chose][0] ) <=0: 
                    print("There are no that item left, we sorry...")
                    return False

            price=self.ITEMS_STORAGES[index]["price"]
            self._chart[chose][0] += quantity
            self._chart[chose][1] = price
            self._total += price * quantity
            print(f"\nNice Choice! you pick: {quantity} {chose}")
            return True
        
        except Exception as e: 
            print(f"{e}")
            return False


    def pay(self)->bool: 
        if not self._checkerleft:
            print("It looks like you still don't have enough money....")
            sleep(2)
            print("Hmmm....")
            sleep(5)
            print('This is akward....')
            sleep(6)
            print("Bye i think....")
            return False

        if (self._financing.balance - self._total) <= 0:
            print("It looks like you  have insufecient fonds...")
            print(f"Well {self._name}. Wny don't you go to the bank? I will wait...")
            self._checkerleft -=1

            return False

        if not self._chart:
            print("You have select anything")
            return False

        #updating the total and balance
        self._financing._balance -= self._total
        self.STOREBANKACCOUNT._balance += self._total #type: ignore
        self._total=0
        self.is_packaging=True

        #updating the stocks
        for key,value in self._chart.items():
            index=my_dict_binary(self.ITEMS_STORAGES,"product",key)
            data=self.ITEMS_STORAGES[index]
            data["stock"]  -= value[0]

            FileManager().update_json(filePath=self.STOCKS,
                                      search_key="id",
                                      search_value=data["id"],
                                      **data)

        self.savepurchaseinfo()
        self._financing.save_info()
        self.STOREBANKACCOUNT.save_info()


        print(f"Now your purchase was done succsesfully dear {self._name}")
        return True

        

    def giveitems(self)->defaultdict|None:
        if not self.is_packaging:
           print("There's nothing to packing...")
           return None

        return self._chart

           


    @classmethod
    def initiation(cls,idbank:int,user:str,/)->Self: 
        """
        This will only create a new class based of simple info
        
        """
        BankOunt().initiation.__doc__
        return cls(financing=BankOunt.initiation(idbank),
                   name=user
                   )


        
    def run(self)->None|defaultdict:
        is_runing:bool=True
        print("-"*50+ " Welcome to Stuffed, Stuff, Soft LTTA. " + "-"*50)

        while is_runing:
            print("1. Select products")
            print("2. Pay chart")
            print("3. Go to the bank")
            print("4 .Exit")

          
            

            select:str=input("What are you going to do: ")


            

            if select =="1": 
                print(f"\nWhat do you want to buy dear {self._name}")

                while True: 
                    try: 
                        print("-"*100)
                        self.display_products_to_sell()
                        print("-"*100)
                        self.display_chart()
                        print("-"*100)
                       

                        chose=input("\nWrite the item wanted (Press q to quite): ")
                        if chose == "q" or chose == "Q": break


                        quantity= int(input("\nHow many?: "))

                        if not self.selecting_stuff(chose,quantity):
                            print("The transation was not complet")

                        sleep(5)
                            
                    except ValueError:
                        print("You need to type a number")
                    except KeyError: 
                        print("It must a number within it the range of products")


            if select =="2": 
                print(f'Wait until everythin is done..., And remember we only acept debit(balance) ')
                
                if not self.pay():
                    print("It looks like you purchase was not comlete")


            if select =="3": 
                self._financing.run()



            if select =="4": 
                is_runing =False

            else:
                print("Type a valid input")
                     
        if self.is_packaging:
            
            return self.giveitems()  

        return None              
        
    @property
    def packing(self):
        return self.is_packaging

    @packing.setter
    def packing(self,___value:bool):
        if not isinstance(___value,bool): raise ValueError("It must be a bool")
        self.is_packaging = ___value 

    @property
    def chart(self):
        return self._chart
    
    @chart.setter
    def chart(self,___value:Mapping[str, list[int|float]] ):
        self._chart = ___value

 


  


      


def main(a:int|None=None)->None:
    """The main funtion """ 
    name:str="Craice Miler"
    id:int=1234
    bag:dict={'books':3,'bottle of water':10,'Snacks':{'candies':7,'chocolate':2}}

    name2:str="Hersy Halston"
    id2:int=1234


    InventaryStore.add_more_stock_existing_product("Wise Owl Plush",5)
    InventaryStore.add_new_products('Candies Pop',5.75,150,Taste='Sweet',Color='Red',Size='small')
    InventaryStore.add_new_products("Wise Owl Plush",10.25,5)
    InventaryStore.add_new_products("Spider Stuffed",24.99,200)





    data=PlushieStore.initiation(id,name2).run()
    if data is not None: 
        print(f"{name} goes to {PlushieStore.__class__} in bought the following: ")
        for k,v in data.items(): 
            print(k,v)

        FileManager().open_file(InventaryStore.DATA)
    else: 
        print("No products")


    print(f"Current bag of {name}")



if __name__ == "__main__":
    main()