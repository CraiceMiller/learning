
def get_three_more_repeated_word(string_list:list)->list:
    count:dict={}
    for i in string_list:
        count[i] = count.get(i,0)+1

    filtering=sorted(count.items(), key=lambda value:value[1], reverse=True)
    only_three:list=[filtering[0][0],filtering[1][0],filtering[2][0],]


    return only_three 

#_g.py
class Bank:
    
    def __init__(self,
                 balance:float=0,
                 wallet:float=0,
                 name:str="user",
                 debt:float=0) -> None:
        
        self.balance=balance
        self.debt=debt
        self.wallet=wallet
        self.name=name

        self.greet()
        self.show_state()

    def greet(self)->None:
        print(f"Grettings {self.name}!")
        return

    def show_state(self)->None:
        print("____your current status_____")
        if self.debt > 0:
            print(f"{self.balance= :,.2f}")
            print(f"{self.wallet= :,.2f}")
            print(f"{self.debt= :,.2f}")
            print("\n")
            
            return 
        print(f"{self.balance= :,.2f}")
        print(f"{self.wallet= :,.2f}")
        print("\n")
        return 

    def withdraw(self,)->None:
        if self.balance <= 0:
            print("INSUFECENT FOUNDS!!!!")
            return 
        
        print("how many do you want withdrawn...")
        amount = None
        while amount is None:
            try :
                validing_amount=float(input())

                if validing_amount > self.balance:
                    print("you can't withdrawn money that you don't have!!")
                    continue 

                if validing_amount <=0:
                    print("it must be greater than zero...")
                    continue 

                amount = validing_amount

            except ValueError:
                print("type a valid input")
             
        
        self.balance -= amount
        self.wallet += amount
        print(f"the amount was sucesfully withdran: current balance")
        Bank.show_state(self)
        return 
    
    def deposit(self)->None:
        if self.wallet <=0:
            print("you don't have nothing to desposit...")
            return 


        print("enter your amount to deposit:")

        amount = None
        while amount == None:
            try:
                validing_amount:float=float(input())
                if validing_amount <=0:
                    print("it must be grater than zero...")
                    continue 
                if validing_amount > self.wallet:
                    print("insufecent fonds!!!")
                    continue


                amount = validing_amount
            except ValueError:
                print("enter a valid amount...")

        self.balance += amount
        self.wallet -= amount
        print("your deposit was sucefully deposited")
        Bank.show_state(self)
        return 
        
    def borrow_money(self)->None:
        if self.debt >= 200:
            print("you need to pay your current debt...")
            return 
        
        print("we can only give you $200")

        borrow = None
        while borrow == None:
            try:
                amount=float(input())

                if amount > 200:
                    print("you can't borrow too mucn!!")
                    continue

                if amount <=0:
                    print("it must be greater than zero!!")
                    continue 

                reach_amount=  200 - self.debt + 1

                if amount >= reach_amount:
                    print("that will reach your debt...")
                    continue 

                self.balance += amount
                self.debt += amount
                borrow = amount
                Bank.show_state(self)
                return 

            except ValueError:
                print("Enter a valid input")

    def pay_debt(self)->None:
        if self.debt <= 0:
            print("don't worry, you don't need to pay anything, have a nice day :)")
            return 
        
        print(f"Pay your current debt {self.debt}")
        
        borrow = None
        while borrow == None:
            try:
                amount=float(input())

                if amount > self.balance:
                    print("INSUFECENTS FONDS!!")
                    continue

                if amount <= 0:
                    print("it must be greater than zero!!")
                    continue 

                if amount > self.debt:
                    print("you are going to pay more..., please just pay the right amount")
                    continue 
                   


                self.balance -= amount
                self.debt -= amount
                borrow = amount
                Bank.show_state(self)
                return 

            except ValueError:
                print("Enter a valid input")
#_m.py
class Store:
    def __init__(self,
                 name='') -> None:
        self.name=name

        self.products={"Plushies":27,"Candies":2.3,"Books":35.5,"Ballons":4}
        self.chart={}
        self.total = 0
        

    def display(self):
        print("\nItems to sell")
        
        for num,(key,values) in enumerate(self.products.items(),start=1):
            print(f"{num}.{key:.<10}${values}")
           
    
    def buy_stuff(self):
        product=[p for p in self.products.keys()]
       
        print(f"\nWhat do you want to buy dear {self.name}")
        while (1):
                try:
                    chose=int(input("Select a number (Press 0 to quite): "))

                    
                    if (chose!=0):
                         if (1 <= chose <= len(product)):
                              quantity=int(input("\nHow many?: "))
                              
                              product_select = product[chose-1] 
                              total_buy= self.products[product_select] * quantity
                              self.total += total_buy
                              
                            
                              self.chart[product_select] = self.chart.get(product_select,0)+ total_buy
                           
                              
                              
                        
                    else:
                         break;
                    
                except ValueError:
                     print("\nType a valid input")
    
    def get_total(self):
         print("\n Your total bill")
         for key,values in self.chart.items():
              print(f"-{key:.<15}${values:,.2f}")
         
         print(f"Total of the purchase is ${self.total:.2f}")

      

