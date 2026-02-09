from banking_program import my_wallet
import random 


def spin_machine()->list[str]:
    symbols:list[str] = ['🦆','🐇','🐈','🧸','🐢']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row:list[str])->None:
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0]==row[1]==row[2]:
        match row[0]:
            case '🦆':
                return bet * 20
            case '🐢':
                return bet*15
            case '🐇':
                return bet*7
            case '🧸':
                return bet*5
            case '🐈':
                return bet*3
    elif row[0]==row[1] or row[1]==row[2] or row[0]==row[2]:
        match row[0] and row[2]:
            case '🦆':
                return bet * 10
            case '🐢':
                return bet*7
            case '🐇':
                return bet*3
            case '🧸':
                return bet*2
            case '🐈':
                return bet*1.25
    else:
        return 0

def main():
    balance = my_wallet()
    print("welcome toe python machine")

    while balance > 0:
        print(f"\nyou current balance is: {balance}")
        print("\nHow much do you wanna lost- I mean invest: ")
        bet = input()
        while not bet.isdigit():
            print("\n please enter a valid input")
            bet = input()

        bet = float(bet)
        

        if bet > balance:
            print("INSUFFINTS FONDS!!")
            continue

        if bet < 0:
            print("it must be grater than zero ")
            continue

        balance -= bet
  
        row = spin_machine()
        print("spinning...\n")
        print_row(row)

        payout=get_payout(row,bet)

        if payout > 0:
            print(f"you have won {payout}\n")
        else:
            print("sorry body,but you have lost this round")

        balance += payout

        print("are you satisfating with that?: ")
        chosse:str=input().lstrip().lower()

        if chosse == 'yes':
            break
    

    print()
    if balance <= 20:
        print(f"you final amount: ${balance:.2f}")
        print("i can't believe you lost so many money")
    else:
        print(f"you final amount: ${round(balance,2):,}")
        print("i hope you enjoy this program :)")




if __name__ == '__main__':
    main()

