def my_wallet(wallet:float=700.00)->float:
    return wallet


def show_balance(balance:float)->None:
    print(f"you current have: ${balance:.2f}")
    print("\r")

def your_account(wallet:float)->float:
    if wallet == 0:
        print("you don't have money to deposited")
        return None
    while True:
        try: 
            print("Enter an amount to be deposited:\r")
            amount:float=float(input())
                            
            if amount<0:
                print("it is not a valid amount")
            elif amount >= wallet +1:
                print("INSUFICIENTS FUNDS!!")
            else:
                return amount
        except ValueError:
            print("Enter a valid input")
            print("\r")
    
def withdraw(balance:float)->float:
    while True:
        try: 
            print("Enter an amount to be withdrawn:")
            amount:float=float(input())
                            
            if amount<0:
                print("the amount must be grater than zero")
                print("\r")
            elif amount > balance:
                print("INSUFICIENTS FUNDS!!")
                print("\r")
            else:
                return amount
        except ValueError:
            print("Enter a valid input")
            print("\r")

def debit_card(balance:float=500)->float:
    return balance

def credit_card(debt)->float:
    diference= 201 - debt

    if debt >= 200:
        print("we can give you more until you pay your current debt !!")
        return None

    
    while True:
        print("how many do you want to borrow?. we can only give $200 in credit:\n")
        try:
            borrow=float(input())
            
            if borrow >200 or borrow <0:
                print("sorry we cant give you that count of mount")
        
            elif borrow >= diference:
                print("if we lend you that amount it will reach your allowed amout !!")
            else:
                return borrow

        except ValueError:
            print("enter a valid input ")

def pay_credit_card(balance, debt)->float:
    if debt == 0:
        print("you don't need to pay anything, you don\'t have debts!!")
        return None


    print("how many are you going to pay?:")
    while True:
        try: 
            amount:float=float(input())
                            
            if amount<0:
                print("the amount must be grater than zero")
                print("\r")
            elif amount > balance:
                print("INSUFICIENTS FUNDS!!")
                print("\r")
            elif (debt - amount) <= 0 :
                print("you are going to pay more, so enter an amount below of your debt....")
            else:
                return amount
            
        except ValueError:
            print("Enter a valid input")
            print("\r")
    

def show_credit_card(debt):
    print("you dont have any debts, have a nice day :)") if debt ==0 else print(f"you need to pay ${debt}")
    print("\r")
 
   



def main():
    wallet= my_wallet()
    balance:float = 0
    debt=0
    is_runnig:bool = True
    while is_runnig:
        print(wallet)
        print(balance)
        print(debt)
        print("----Banking program----")
        print("1. Show Balance")
        print("2. Deposite money")
        print("3. withdraw money")
        print("4. borrow money")
        print("5. pay the credit card")
        print("6. show the credit card")
        print("7. Debit card")
        print("8. Exit")

        print("What do you want to do?")
        choice:int= input()

        match choice:
            case "1":
                show_balance(balance)
                print("\r")
            case "2":
                x = your_account(wallet)
                if x != None:
                 balance+=x
                 wallet -=x
                print("\r")
            case "3":
                x=withdraw(balance)
                balance-=x
                wallet+=x
                print("\r")
            case "4":
                x = credit_card(debt)
                if x != None:
                    debt += x
                    balance += x

                print("\r")
            case "5":
                x= pay_credit_card(balance,debt)
                if x != None:
                  debt -= x
                  balance -= x
                print("\r")
            case "6":
                show_credit_card(debt)
                print("\r")
            case "7":
                x=debit_card(balance)
                print(x)
                print("\r")
            case "8":
                is_runnig=False
                print("\r")
            case _:
                print("please write a vlaid input :|")
                print("\r")



if __name__ == "__main__":
    main()

print("bye master :3")