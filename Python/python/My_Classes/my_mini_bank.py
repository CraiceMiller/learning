
class Bank:
    
    def __init__(self,
                 balance:float|int=0,
                 wallet:float|int=0,
                 name:str="user",
                 debt:float|int=0) -> None:
        
        self.balance=balance
        self.debt=debt
        self.wallet=wallet
        self.name=name

        self.greet()
        

    def greet(self):
        print(f"Grettings {self.name}!")
        return

    def show_state(self):
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

    def withdraw(self,):
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
    
    def deposit(self):
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
        
    def borrow_money(self):
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

    def pay_debt(self):
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




def main_bank(user:Bank):

    person:Bank=user
    is_runnig:bool = True

    while is_runnig:
        print("----Banking program----")
        print("1. Show Balance")
        print("2. Deposite money")
        print("3. withdraw money")
        print("4. borrow money")
        print("5. pay the credit card")
        print("6. Exit")

        print("What do you want to do?")
        choice= input()

        match choice:
            case "1":
                person.show_state()
                print("\r")

            case "2":
                person.deposit()
                print("\r")

            case "3":
                person.withdraw()
                print("\r")

            case "4":
                person.borrow_money()
                print("\r")

            case "5":
                person.pay_debt()
                print("\r")
           
            case "6":
                is_runnig=False
                print("\r")

            case _:
                print("please write a vlaid input :|")
                print("\r")





