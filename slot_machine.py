# Slot machine
import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔" ,"⭐"]
    # result =[]

    return[random.choice(symbols) for symbol in  range(3)]

    # for symbol in range(3):
    #     result.append(random.choice(symbols)) 
    # return result


def print_row(row):
    print("*****************************")
    print(" | ".join(row))
    print("*****************************")
def get_payout(row, bet):
    if row[0] == row[1]== row[2]:
        if row[0] == '🍒':
            return bet*3
        elif row[0]== "🍉":
            return bet*4
        elif row [0] == "🍋":
            return bet*5
        elif row[0] == "🔔":
            return bet*10
        elif row[0] == "⭐":
            return bet*20
    return 0

def main():
    Balance = 100

    print("*****************************")
    print("Welcome to Python Slots ")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("*****************************")
    
    while Balance > 0 :
        print(f"Current balance: ${Balance}")

        bet = input("Please your bet amount: ")

        if not bet.isdigit():
            print("Please Enter a valid Number")
            continue

        bet = int(bet)

        if bet>Balance:
            print("Insufficient funds")
            continue

        if bet <=0:
            print("Bet must be greater than 0")
            continue
        
        Balance -= bet

        row = spin_row()
        # print(row)
        print("Spining...\n")
        print_row(row)
        payout = get_payout(row, bet)

        if payout >0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round") 

        Balance += payout 

        if Balance == 0:
            new_Balance = int(input("Do You want to play again? Please add new balance: "))
            Balance += new_Balance

        spin_again = input("Do you want to spin again? (Y/N) ").capitalize()
        
        if  spin_again != "Y":
            break
    print("*****************************")
    print(f"Game Over! Your Final Bilance is ${Balance}")
    print("*****************************")

        



if __name__ == '__main__':
    main()