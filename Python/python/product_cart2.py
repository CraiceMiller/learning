class Product: 
    total_products_created:int=0

    def __init__(self, name:str, price:float,quantity:int) -> None:
        self.name=name
        self.price=price
        self.quantity=quantity

        Product.total_products_created+=1


    def display_info(self)->None:
        print(f"{self.name:<20}{self.price:<20}{self.quantity:<20}")

    def add_stock(self, amount:int)->None:
        if amount <=0:
            print("the amount should be a positive number!!")
        else:
            self.quantity += amount

    def sell_item(self, amount:int)->None:
        if  amount <= 0:
            print("it should be a positive number!!")
            print("\n")

        elif amount > self.quantity:
            print("INSUFFICIENT STOCKS!!!")
            print("\n")

        else:
            self.quantity -= amount
            print(f"the order have been compled sucesfully, you have bought {amount} {self.name}")
            print("\n")

    @classmethod
    def get_total_products_count(clas)->None:
        print(f"the total of products is {clas.total_products_created}")


list_of_productos:dict[str,str]={}
print("------CREATING PRODUCTS-------")
product1:Product = Product("computer", 950.75,42)
product2:Product = Product("Tablets", 500,30)
product3:Product = Product("Phone", 455.5,65)
product4:Product = Product("Televisions", 863.45,52)
print("\n")


print("------TOTAL OF PRODUCTS CREATED -------")
print(Product.total_products_created)
print("\n")

print("------PROUDCT INFO -------")
def list_product()->None:
    print(f"{"Product":<20}{"Price":<20}{"In Stock":<20}")
    product1.display_info()
    product2.display_info()
    product3.display_info()
    product4.display_info()

list_product()
print("\n")

print("------STOCKS OPERATIONS -------")
#adding new stocks
product2.add_stock(20)
product4.add_stock(5)

#sell items
product1.sell_item(50)
product3.sell_item(30)
product2.sell_item(0)
product3.sell_item(23)
product2.sell_item(15)
product4.sell_item(75)

print("wait we are adding more stocks")
print("...")
#adding more stocks
product4.add_stock(35)

#sell again
product4.sell_item(75)



print("\n")


print("------ADDING MORE PRODUCTS -------")
def new_list_product()->None:
    print(f"{"Product":<20}{"Price":<20}{"In Stock":<20}")
    product1.display_info()
    product2.display_info()
    product3.display_info()
    product4.display_info()
    product5.display_info()
    product6.display_info()


product5:Product = Product("Radios", 150,85)
product6:Product = Product("Printers", 624.85,47)

print("------TOTAL OF PRODUCTS CREATED -------")
Product.get_total_products_count()
print()
new_list_product()










