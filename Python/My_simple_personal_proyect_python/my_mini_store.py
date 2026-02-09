#here i wanna create a script where storage product, price, stock and details of each item...
#and where i coustumer can buy it what evet of them

from iterables_to_use import plushy_store_items
from copy import deepcopy
from my_mini_bank import *


#This is where Every product will be storage...
class InventaryStore:
    #This class will only storage every product as a dict within a list...
    ITEMS_STORAGES:list[dict]=plushy_store_items

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
                    

            print('\n')
                
                
            
        return None

    @classmethod
    def display_quantity_product(cls)-> None:
        print(f"Curretly we have {len(cls.ITEMS_STORAGES)} differents products")
        return None
    
    @classmethod
    def add_more_stock_existing_product(cls,
                                        product_name:str,
                                        more_stock:int
                                        )->None:
        """
        Description:
        This method will create more stock to an specif existing product
        """
        get_product=[product for product in cls.ITEMS_STORAGES if product.get('product') == product_name]
        if not get_product:
            print('Product not found!!')
            return 
        
        print(f"Old stock: {get_product[0].get('stock')}")
        get_product[0]['stock']=get_product[0].get('stock',0) + more_stock
        print(f"Currently stocks: {get_product[0].get('stock')}")
        print(f'The stock of {get_product[0].get('product')} has uppdate successfully ')
        return 

#this class will only add new  products to the InventaryStore...
class Product(InventaryStore):
    #this class will only add new  products to the InventaryStore...
    def __init__(self,
                 name:str,
                 price:float,
                 stocks:int,
                 extra_info:dict|None=None
                 ) -> None:
        
        self._name:str=name
        self._price:float=price
        self._stocks:int=stocks
        self._extra_characteristics=extra_info 

        if extra_info is not None:
            adding_new_product:dict= {
            "product": name,
            "price": price,
            "stock": stocks,
            "extra_characteristics":extra_info
            }
            InventaryStore.ITEMS_STORAGES.append(adding_new_product)
        else:
            adding_new_product2:dict= {
            "product": name,
            "price": price,
            "stock": stocks
            }
            InventaryStore.ITEMS_STORAGES.append(adding_new_product2)

        

    
    def display_info(self) -> None:
        print(f'{self._name}: ${self._price}')

#this will only create the new product
def create_new_product(_product:str,
                   _price:float,
                   _stock:int,
                   **_extra_info
                   )->None:
    """
    Description:
    This funtion only add all the info to the Product class
    """
    if _extra_info:
         Product(
        name=_product,
        price=_price,
        stocks=_stock,
        extra_info=_extra_info
    )
    else:
        Product(
        name=_product,
        price=_price,
        stocks=_stock,
     
    )
    print(f'The product: {_product}, has succesfully added to the inventary')
   
#this is where i sell all my stuff 
class PlushieStore(InventaryStore):
    def __init__(self,
                 financing:Bank,
                 bag:dict,
                 name:str="User"
                 ) -> None:
        
        self.name:str=name
        self.financing=financing
        self.bag=bag


        self.products:list=InventaryStore.ITEMS_STORAGES
        self.chart:dict={}
        self.how_many_gonna_buy:dict={}
        self.total:int|float = 0
        self.is_packaging:bool=False

        PlushieStore.message()

    @staticmethod
    def message():
        print("-"*50+ " Welcome to Happy-Plushie Store S.A. " + "-"*50)
        


    def display_products_to_sell(self)->None:
        """
        Description: 
        This only display a list of every product in the inventary
        """
        products_selling=[p.get('product') for p in self.products]
        prices_selling=[price.get('price') for price in self.products]
        
        print("\nItems to sell".title())
        
        for num,(key,values) in enumerate(zip(products_selling, prices_selling),1):
                print(f"{num}.{key:.<40}${values}")
           
    def selecting_stuff(self):
        """
        Desciption:
        In this method the user can buy anything they want...
        """
        product=[p for p in self.products]
        accumulated_stocks:dict={}
       
        print(f"\nWhat do you want to buy dear {self.name}")
        while (1):
                try:
                    chose=int(input("Select a number (Press 0 to quite): "))

                    
                    if (chose!=0):
                         
                         
                         if (1 <= chose <= len(product)):
                              

                              if (product[chose-1].get('stock')-accumulated_stocks.get(product[chose-1].get('product'),0)) == 0:
                                  print(f"WE really sorry, but we run out of {product[chose-1].get('product')}")
                                  continue
                              

                              print(f"\nYou pick: '{product[chose-1].get('product')}', Great Choice!!, in stocks are {product[chose-1].get('stock')-accumulated_stocks.get(product[chose-1].get('product'),0)}")
                              quantity= int(input("\nHow many?: "))

                              if quantity > (product[chose-1].get('stock')-accumulated_stocks.get(product[chose-1].get('product'),0)):
                                  print("We sorry but the is out of the range of stocks...")
                                  continue
                              
                              product_select= product[chose-1]
                              total_buy=product_select['price'] * quantity
                              self.total += total_buy
                             
                              
                              self.chart[product_select.get('product')] = self.chart.get(product_select.get('product'),0)+total_buy
                              self.how_many_gonna_buy[product_select.get('product')] = self.how_many_gonna_buy.get(product_select.get('product'),0)+ quantity
                              accumulated_stocks[product_select.get('product')] = accumulated_stocks.get(product_select.get('product'),0)+quantity
                             
                              
                             
                           
                              
                              
                        
                    else:
                         accumulated_stocks.clear()
                         break;
                    
                except ValueError:
                     print("\nType a valid input")
    
    def show_chart_before_to_buy(self):
         """
         Description: this only will give the list of thing to buy
         """
         print("\n Resume of your purchase so far")
         products=[p for p in self.chart.keys()]
         prices=[p for p in self.chart.values()]
         quantities=[q for q in self.how_many_gonna_buy.values()]
  
         for key,price,quantity in zip(products,prices,quantities):
              print(f"You're going to buy {quantity} '{key}' with the total of ${price:,.2f}")
         
         print(f"Total of the purchase will be ${self.total:,.2f}")

    def pay_chart(self):
        """
        Description: this method will ask the user to pay it.
        """
        self.financing.show_state()
        desicion=input(f"Dear {self.name} type 'yes' to finished the purchase: ").lstrip().lower()
        if (desicion!='yes'):
            print("Ok, so hmmmm, you can go, Bye...!")
            self.chart.clear()
            self.how_many_gonna_buy.clear()


        else:
           print(f'Wait until everythin is done..., And remember we only acept debit(balance) ')
           from time import sleep
           sleep(5)


           if (self.financing.balance - self.total) <0:
               print("It looks like you  have insufecient fonds...")
               print(f"Well {self.name}, do you want to go to the bank?")
               go_bank:str=input().lstrip().lower()

               if go_bank == 'yes':
                   main_bank(self.financing)

                   if (self.financing.balance - self.total) <0:
                       print("It looks like you still don't have enough money....")
                       sleep(2)
                       print("Hmmm....")
                       sleep(5)
                       print('This is akward....')
                       sleep(6)
                       print("Bye i think....")
                       self.chart.clear()
                       self.how_many_gonna_buy.clear()


                   else:
                       print("It looks like you have enough money now...")
                       #updating the total and balance
                       self.financing.balance -= self.total
                       self.total=0
                       #updating the stocks
                       for products in InventaryStore.ITEMS_STORAGES:
                                for key,values in self.how_many_gonna_buy.items():
                                    if products.get('product') == key:
                                        products['stock'] = products["stock"] - values  
                    

                    
                       print(f"Now your purchase was done succsesfully dear {self.name}")
                       self.financing.show_state()
                       self.is_packaging=True

                   


               else:
                   print("Ok, so hmmmm, you can go now, until you got money")
                   self.chart.clear()
                   self.how_many_gonna_buy.clear()


           else:
               #updating the total and balance
               self.financing.balance -= self.total
               self.total=0
               #updating the stocks
               for products in InventaryStore.ITEMS_STORAGES:
                   for key,values in self.how_many_gonna_buy.items():
                       if products.get('product') == key:
                           products['stock'] = products["stock"] - values
                

                
               print(f"Your purchase was done succsesfully dear {self.name}")
               self.financing.show_state()
               self.is_packaging=True
               

    def PACKAGING(self):
        if self.is_packaging:
           self.chart.update(self.how_many_gonna_buy)
    

           new_stuff={'Plushies': self.chart}
           copy_new_stuff=deepcopy(new_stuff)
           self.bag.update(copy_new_stuff)
         
           
           #updating againg the chart
           self.chart.clear()
           self.how_many_gonna_buy.clear()
        else:
            print("There's nothing to packing...")
           

