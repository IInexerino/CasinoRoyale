from alive_progress import alive_bar
from time import sleep

def showBalance(TOTAL_BALANCE):
    print("\n------------------------------------------------------------")
    print(f"Your current balance is: ${TOTAL_BALANCE}")
    print("------------------------------------------------------------")


def deposit(TOTAL_BALANCE, PERSONAL_WALLET_BALANCE):
    while True:
        print(f"\nYour current personal wallet balance is: ${PERSONAL_WALLET_BALANCE}")
        amount = input("\nHow much would you like to deposit: $")
        if amount.isdigit(): #checks if it is a digit
            amount = int(amount)
            if amount > 0:
                if amount <= PERSONAL_WALLET_BALANCE:
                    TOTAL_BALANCE += amount

                    PERSONAL_WALLET_BALANCE -= amount
                    
                    with alive_bar(amount, title="Processing the final outcome: ") as bar:
                        for _ in range(amount):
                            bar()
                            sleep(0.01)

                    print("\n------------------------------------------------------------")
                    print(f"\nYour new personal wallet balance is: ${PERSONAL_WALLET_BALANCE}")
                    while True:
                        wyltc = input("Would you like to deposit again? (y/n): ")
                        if wyltc not in ["y", "n"]:
                            print("Enter a valid input")
                            continue
                        elif wyltc == "y":
                            break
                        else: 
                            break
                    if wyltc == "n":                    
                        return TOTAL_BALANCE, PERSONAL_WALLET_BALANCE
                    
                else:
                    print("\nYou one broke ass mf. You cant spend money you dont have!")
                    return TOTAL_BALANCE, PERSONAL_WALLET_BALANCE
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter an integer.")


def withdraw(TOTAL_BALANCE, PERSONAL_WALLET_BALANCE):
    while True:
        amount = input("\nHow much would you like to withdraw: $")
        if amount.isdigit(): #checks if it is a digit
            amount = int(amount)
            if amount > 0:
                if amount <= TOTAL_BALANCE:
                    PERSONAL_WALLET_BALANCE += amount

                    TOTAL_BALANCE -= amount
                    
                    with alive_bar(amount, title="Processing the final outcome: ", bar="brackets") as bar:
                        for _ in range(amount):
                            bar()
                            sleep(0.01)

                    print("\n------------------------------------------------------------")
                    print(f"\nYour new personal wallet balance is: ${PERSONAL_WALLET_BALANCE}")
                    while True:
                        wyltc = input("Would you like to withdraw again? (y/n): ")
                        if wyltc not in ["y", "n"]:
                            print("Enter a valid input")
                            continue
                        elif wyltc == "y":
                            break
                        else: 
                            break
                    if wyltc == "n":                    
                        return TOTAL_BALANCE, PERSONAL_WALLET_BALANCE

                else:
                    print("\nAaah, you think we're stupid! You cannot withdraw money that is not yours *yet*.")
                    sleep(2)
                    return TOTAL_BALANCE, PERSONAL_WALLET_BALANCE
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter an integer.")
