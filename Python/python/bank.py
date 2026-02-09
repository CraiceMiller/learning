



#class method
class Bank:
    """
    DESCRIOPTION: 
        This is just a very basic bank class where you can do simple things 
        like watch your current balance, pay to debt and only
    
    UPDATE: 
    one day of may 
    one day of june 
    22/08/2025
    
    """
    
    CREDIT_CARD:float=200
    TAX_RATE:float=0.05

    #Dunder methods 
    def __init__(self,
                 balance:float=0,
                 wallet:float=0,
                 debt:float=0, 
                 name:str="user",
                 user:str="N/A",
                 password:str="N/A",
                 id: int = 0) -> None:
        """
        PARAMETERS: 

            balance: This is the currently money user has
            wallet: resemble a normal wallet. All this money will not be consider a method to pay
            name: The user name, user as a default 
            debt: if the user has debt
        
        Example: 
            >>> Bank(500,100,"Craice")
                #this will solely create a Bank object to work with
        
        """
        
        self._balance=round(balance,2)
        self._debt=round(debt,2)
        self._wallet=round(wallet,2)
        self._name=name
        self._id=round(id,2)
        self._user=user
        self._password=password

     

    def __str__(self) -> str:
        return f"User: {self._name}      Balence: {self._balance}"
    
    def __eq__(self, __value) -> bool:
        return self._name == __value._name
    
    def __lt__(self,__value)->bool:
        return self._balance < __value._balance
    
    def __gt__(self,__value)->bool:
        return self._balance > __value._balance
    
    def __add__(self, __value)->int|float:
        return self._balance + __value._balance
    
    def __contains__(self,keyword:str)->bool:
        return keyword in self._name 

    def __getitem__(self, key:str)->str:
        if key == "user":
            return self._name
        return 'N/A'
    
    def __repr__(self) -> str:
        return f"Bank(_name={self._name},_balance={self._balance},_debt={self._debt},_wallet={self._wallet},)"\
                f"_id={self._id},password={self._password}, user={self._user}"

    def __hash__(self) -> int:
        return hash(self._name)
    
    #helper methods 
    def validing_amount(self,amount:float,reason:float)->bool:
        """This method will valid a certain amoumt"""
        is_valid:bool=True

        try: 

        
            if amount > reason:
                print("INSUFECENTS FONDS!!")
                is_valid=False
                

            if amount <=0:
                print("it must be greater than zero...")
                is_valid= False

            return is_valid
        
        except: 
            return False
        

    def validing_CREDIT_CARD(self,amount:float)->bool: 
        try: 
            if amount > self.CREDIT_CARD:
                print("you can't borrow too mucn!!")
                return False
                    

            if amount <=0:
                print("it must be greater than zero!!")
                return False
                        

            reach_amount=  self.CREDIT_CARD - self._debt + 1

            if amount >= reach_amount:
                print("that will reach your _debt...")
                return False
                        

            return True
        

        except: 
            return False



    #Instances methods
    def greet(self)->str:
        "This only print a message to greet the user"
        return f"Grettings {self._name}!"


    def show_state(self)->None:
        """This only print the current state of the user"""
        print("\n")
     


        print("____your current status_____")
        if self._debt > 0:
            print(f"{self._balance= :,.2f}")
            print(f"{self._wallet= :,.2f}")
            print(f"{self._debt= :,.2f}")
            print("\n")
            return 
        
        print(f"{self._balance= :,.2f}")
        print(f"{self._wallet= :,.2f}")
        print("\n")
        

    def withdraw_amount(self,
                 amount:float|None=None)->bool:
        """
        DESCRIPTION: 
            This method will try to withdraw money, and storage. If the balance is equals or 
            less than zero will do nothig. If the user type another non-valid data(it must be only 
            a number) will print an error message. If the transation was successful, it wil update 
            the data towards the current user's info by subtraction the currently balance and updating into 
            the wallet. If the transaction was not succesfull, then will return Fasle

        Return :    
            A bool meaning that the transation was succesfully done or not

        Example: 
            >>> Bank(balance=100).withdraw(-100)
                output:False
                #This means the balnce does not change 
        
        """
        if self._balance <= 0:
            print("INSUFECENT FOUNDS!!!!")
            return False
        
        print("how many do you want withdrawn...")
       
        while amount is None:
            try :
                validing_=float(input())

                if self.validing_amount(validing_,self._balance):
                    amount = validing_  

            except ValueError:
                print("type a valid input")

        if not self.validing_amount(amount,self._balance): 

            return  False
        
        amount = round(amount,2)
        
        self._balance -= amount
        self._wallet += amount
        print(f"the amount was sucesfully withdran: current _balance")

        self.show_state()
        return True
    
    def deposit(self,
                amount:float|None=None)->bool:
        """
        DESCRIPTION: 
            This method will try to deposit money from the wallet, and storage into the balnce.
             If the balance is equals or 
            less than zero will do nothig. If the user type another non-valid data(it must be only 
            a number) will print an error message. If the transation was successful, it wil update 
            the data towards the current user's info. If the transaction was not succesfull, then will return Fasle

        Return :    
            A bool meaning that the transation was succesfully done or not

        Example: 
            >>> Bank(balance=100,wallet=).deposit('pizza')
                output:False
                #This means the wallet does not change 
        
        """
        
        if self._wallet <=0:
            print("you don't have nothing to desposit...")
            return False


        print("enter your amount to deposit:")

     
        while amount is None:
            try:
                validing_:float=float(input())

                if self.validing_amount(validing_,self._wallet):
                 amount = validing_

            except ValueError:
                print("enter a valid amount...")


        if not self.validing_amount(amount,self._wallet): 
            return False

        amount = round(amount,2)
        self._balance += amount
        self._wallet -= amount
        
        print("your deposit was sucefully deposited")
        self.show_state()
        return True
        
    def borrow_money(self,
                     borrow:float|None=None)->bool:
        """
        DESCRIPTION: 
            This method will resemble a credit card, and you can borrow only the 
            amount that the bank allow,

        Return: 
            a bool meaning that the transaticion was successfully done

        Example: 
            current Credit allow: ${self.CREDIT_CARD}

            >>> Bank(100,50,10).borrow_money(100)
            output: True
        
        
        """
        credit:float=self.CREDIT_CARD

        if self._debt >= credit:
            print(f"you need to pay your current debt: {self._debt}")
            return False
        
        print(f"we can only give you ${credit - self._debt}")

        try: 

            while borrow == None:
                
                amount=float(input())

                if self.validing_CREDIT_CARD(amount): 
                    borrow = amount
                


            if not self.validing_CREDIT_CARD(borrow): 
                return False


            self._balance += amount
            self._debt += amount
            borrow = amount
            self.show_state()
            return True 


        except ValueError:
                print("Enter a valid input")
                return False




    def pay__debt(self,borrow:float|None=None)->bool:
        """This will try to pay the current debt"""
        if self._debt <= 0:
            print("don't worry, you don't need to pay anything, have a nice day :)")
            return False
        
        print(f"Pay your current _debt {self._debt}")
        
        try: 
      
            while borrow is None:
            
                amount=float(input())

                if amount > self._debt:
                    print("you are going to pay more..., please just pay the right amount")
                    continue 

                if self.validing_amount(amount,self._balance):
                    borrow = amount

             
            if not self.validing_amount(borrow,self._balance): 
                return False

            borrow = round(borrow,2)
            self._balance -= borrow + (borrow * self.TAX_RATE)
            self._debt -= borrow 
    
            self.show_state()
            return True

        except ValueError:
            print("Enter a valid input")
            return False

    #Main method
    def run(self)->None:
        """This method will only apply everyting of this class"""

        print(self.greet())

        is_runnig:bool = True

        while is_runnig:
            print("----Banking program----")
            print("1. Show _balance")
            print("2. Deposite money")
            print("3. withdraw money")
            print("4. borrow money")
            print("5. pay the credit card")
            print("6. Exit")

            print("What do you want to do?")
            choice= input()

            match choice:
                case "1":
                    self.show_state()
                    print("\r")

                case "2":
                    self.deposit()
                    print("\r")

                case "3":
                    self.withdraw_amount()
                    print("\r")

                case "4":
                    self.borrow_money()
                    print("\r")

                case "5":
                    self.pay__debt()
                    print("\r")
            
                case "6":
                    print(f"Bye {self._name}!")
                    is_runnig=False
                    print("\r")

                case _:
                    print("please write a vlaid input :|")
                    print("\r")


    @staticmethod
    def validing_number(number)->None: 
        """This is just a serie of raise with the aim of ensure that the value is 
        a valid input"""


        if not isinstance(number,float|int): 
            raise ValueError(f"{number} is not a number. It must be a number")
        
        if number <0: 
            raise ValueError(f"the number {number} Must be greater than zero")
        
       


    #creating the properties    
    #Balance   
    @property
    def balance(self)->float: 
        return self._balance
    
    @balance.setter
    def balance(self,value:float)->None:
        self.validing_number(value)
        print(f"Balance: {self._balance} is now {value}")
        self._balance = value

    @balance.deleter
    def balance(self)->None:
        print(f"balance atribute was succesfully delate from this class ")
        del self._balance



    #wallet
    @property
    def wallet(self)->float: 
        return self._wallet
    
    @wallet.setter
    def wallet(self,value:float)->None:
        self.validing_number(value)
        print(f"Wallet: {self._wallet} is now {value}")
        self._wallet = value

    @wallet.deleter
    def wallet(self)->None:
        print(f"wallet atribute was succesfully delate from this class ")
        del self._wallet


    #name
    @property
    def name(self)->str:
        return self._name

    @name.setter
    def name(self,value:str)->None:
        print(f"Name: {self._name} is now {value}")
        self._name = value

    @name.deleter
    def name(self)->None: 
        print(f"The user {self._name} was delate")
        del self._name


    #debt
    @property
    def debt(self)->float:
        return self._debt
    
    @debt.setter
    def debt(self,value:float)->None:
        self.validing_number(value)
        print(f"Debt: {self._debt} is now {value}")
        self._debt = value

    @property 
    def id(self): 
        return self._id
    
    @id.setter 
    def id(self, value:int)->None: 
        if not isinstance(value,int): 
            raise ValueError("The value must a number")

        self._id =value

    @property
    def user(self): 
        return self._user 
    
    @user.setter 
    def user(self, value:str):
        if not isinstance(value,str): 

            raise ValueError(F"{value} must be a string") 


        print(f"{self._user} change to {value }")
        self._user = value 

    @property 
    def password ( self): 
        return self._password
    
    @password.setter 
    def password(self, value:str): 
        if not isinstance(value,str): 
            raise ValueError(F"{value} must be a string") 

        print(f"{self._password} chas to {value}")
        self_password= value



    #class methods
    @classmethod
    def value(cls): 
        return cls("hello")
 
    
