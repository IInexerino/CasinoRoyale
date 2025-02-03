import casinoGame_slotMachine 
import casinoGame_numberGuessing
from banking_functions import *

TOTAL_BALANCE = 0
PERSONAL_WALLET_BALANCE = 0

print("")
PERSONAL_WALLET_BALANCE += int(input("How much money do you take with you to the casino: $"))



def main_game_menu():
    global PERSONAL_WALLET_BALANCE
    global TOTAL_BALANCE
    while True:
        print("\n\n------------------------------------------------------------")
        print("\nW E L C O M E   T O   C A S I N O  -  R O Y A L E")
        print("\nHere the miserable get rich, and the rich get miserable.")
        print("\n------------------------------------------------------------")
        print(f"\nYou brought ${PERSONAL_WALLET_BALANCE} with you.")
        print("\n------------------------------------------------------------")
        selected_menu_option = input("\nChoose what you would like to do:\n\n1. Number guessing game\n2. Slot machine game\na. Display your current casino account balance and either deposit more or withdraw.\nb. Quit the Casino.\n\n> ")

        if selected_menu_option == "1":
            casinoGame_numberGuessing.main()

        elif selected_menu_option == "2":
            casinoGame_slotMachine.main(TOTAL_BALANCE, PERSONAL_WALLET_BALANCE)
        
        elif selected_menu_option == "a":
            showBalance(TOTAL_BALANCE)
            while True:
                selected_menu_option3 = input("\nWould you like to:\n1. Deposit from your personal wallet\n2. Withdraw from your CasinoRoyale account.\n3. Go back to the main menu\n\n> ")
                if selected_menu_option3 not in ["1", "2", "3"]:
                    print("Enter a valid input.")
                    continue
                elif selected_menu_option3 == "1":
                    showBalance(TOTAL_BALANCE)
                    TOTAL_BALANCE, PERSONAL_WALLET_BALANCE = deposit(TOTAL_BALANCE, PERSONAL_WALLET_BALANCE)
                    break
                elif selected_menu_option3 == "2":
                    TOTAL_BALANCE, PERSONAL_WALLET_BALANCE = withdraw(TOTAL_BALANCE, PERSONAL_WALLET_BALANCE)
                    break
                elif selected_menu_option3 == "3":
                    break

        elif selected_menu_option == "b":
            exit()

        else:
            print("Enter a valid input.")

main_game_menu()