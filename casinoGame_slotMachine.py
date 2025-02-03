import random
from alive_progress import alive_bar
from time import sleep

from insult_generator import youABrokeBoy_insult_generator
from banking_functions import *

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_dict = {
    " Stone " : 100,
    " Coal  " : 11,
    "Bronze " : 9,
    " Iron  " : 7,
    " Gold  " : 5,
    "Diamond" : 3
}

symbol_value = {
    " Stone " : 2,
    " Coal  " : 3,
    "Bronze " : 5,
    " Iron  " : 6,
    " Gold  " : 8,
    "Diamond" : 10
}

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])


def check_winnings_and_add_to_TOTAL_BALANCE(columns, lines, bet, values, TOTAL_BALANCE):
    round_winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_test = column[line]
            if symbol != symbol_to_test:
                break
        else:
            round_winnings += values[symbol] * bet
    
    TOTAL_BALANCE += round_winnings
    return round_winnings, TOTAL_BALANCE


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): # itterates through every kay-value pair of symbol_dict and assigns it to the two variables through each itteration
        for _ in range(symbol_count): # itterates a number of times proportionate to the magnitude of each corresponding value in symbol_dict
            all_symbols.append(symbol) # adds one instance of key [symbol] as an item into the all_symbols list, for each symbol, and for each integer in corresponding magnitude (counts all of the symbols in the table and writes them out)

    columns = []
    for col in range(cols): # itterates through each preset column of the slot machine
        column = []
        current_symbols = all_symbols[:] # copies the list of all_symbols into current_symbols
        for _ in range(rows): # itterates through each item (on each row) of the column
            value = random.choice(current_symbols) # each spinning wheel has a preset amount of possible outcomes that cannot be duplicated, this randomly choses a symbol from the current_symbols list and assigns it to value
            current_symbols.remove(value) # this removes the previously rolled possible outcome from the future pool [our list current_symbols] of possible outcomes
            column.append(value) # adds a value to column for each row in the column we go down
            
        columns.append(column) # adds a column list to columns for each column itterated through
    
    return columns # returns the list of columns which are lists of values within the rows in descending order


def print_slot_machine(columns): #transposition
    print("\n------------------------------------------------------------")
    for row in range(len(columns[0])):
        print('                   ', end = "")
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end =" | ")
            else:
                print(column[row], end = "")

        print()
    print("------------------------------------------------------------\n")



def get_number_of_lines():
    while True:    
        lines = input("\nEnter the amount of lines you would like to bet on, starting with the top line (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter an integer.")

    return lines


def get_bet():
    while True:
        amount = input("\nHow much would you like to bet on each line: $")
        if amount.isdigit(): #checks if it is a digit
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
        else:
            print("Please enter an integer.")

    return amount
    

def configure_and_spin_slot_machine(TOTAL_BALANCE):
    lines = get_number_of_lines()
    bet = get_bet()
    insult = youABrokeBoy_insult_generator()
    total_bet = bet * lines
    if total_bet > TOTAL_BALANCE:
        print(f"\nYour balance is ${total_bet - TOTAL_BALANCE} short, your current balance is ${TOTAL_BALANCE}. Go get some money broke boy, you're {insult}.")
        return
    
    print(f"You are betting ${bet} on {lines} lines.")

    while True:
        if total_bet <= TOTAL_BALANCE:   
            print(f"Total bet is equal to: ${total_bet}")
            TOTAL_BALANCE -= total_bet

            # all cosmetic
            with alive_bar(1000, bar="fish", title="Spinning your slots: ") as bar:
                for _ in range(1000):
                    if _ % 100 == 0:
                        slotsVisual = get_slot_machine_spin(ROWS, COLS, symbol_dict)
                        print_slot_machine(slotsVisual)
                    sleep(0.005)
                    bar()
            with alive_bar(1000, title="Processing the final outcome: ") as bar:
                for _ in range(1000):
                    bar()
                    sleep(0.0025)

            # determination of real, final slot-grid outcome
            slots = get_slot_machine_spin(ROWS, COLS, symbol_dict)
            print_slot_machine(slots)
            print("------------------------------------------------------------\n")
            
            # checks for round winnings
            round_winnings, TOTAL_BALANCE = check_winnings_and_add_to_TOTAL_BALANCE(slots, lines, bet, symbol_value, TOTAL_BALANCE)
            resulting_adjustment = round_winnings - total_bet
            previous_balance = TOTAL_BALANCE - round_winnings + total_bet
            print(f"All in all, you have bet ${total_bet}, and won ${round_winnings} from the house, leaving you with the total result of ${resulting_adjustment}.")
            print("\n------------------------------------------------------------")
            print(f"Your previous balance is: ${previous_balance}")
            print(f"Your current balance is: ${TOTAL_BALANCE}")
            print("------------------------------------------------------------\n")

            if TOTAL_BALANCE > previous_balance:
                print(f"Your balance has increased by {truncate(float(TOTAL_BALANCE - previous_balance) / previous_balance * 100.0, 2)}%!!! You can already smell your next win, which is only a few more clicks away!")
            if TOTAL_BALANCE < previous_balance:
                insult  = youABrokeBoy_insult_generator()
                print(f"Your balance has decreased by {truncate(float(previous_balance - TOTAL_BALANCE) / previous_balance * 100.0, 2)}%. I can already sense the communism eminating from you, you {insult}. Don't blame the system, you only have yourself to blame. If only you had more money to gamble you would not be wallowing around in your communistic anguish just about now. Spend the rest of your money with me. Spend the rest of your life with me.\n\nI am your only possible lover, the slot machine...")
            print("\n------------------------------------------------------------")
            
            # ask to spin again or go to menu
            while True:
                re_spin = input(f"\nWould you like to:\n\n1. Spin again, with the same settings\n2. Go back to the menu\n\n> ")
                print("------------------------------------------------------------\n\n")
                if re_spin not in ["1", "2"]:
                    print("\nEnter a valid input")
                    continue
                else:
                    break
            if re_spin == "1":
                continue
            elif re_spin == "2":
                break
        
        else:
            print("\nYou are too low on funds to continue. You will be escorted out of the slotroom into the casino by bodyguards.")
            break


# main menu of the slot game
def action_menu(TOTAL_BALANCE, PERSONAL_WALLET_BALANCE): 
    showBalance(TOTAL_BALANCE)
    print("\n\n------------------------------------------------------------")
    selected_menu_option = input(f"\nChoose what you would like to do:\n\n1. Would you like to deposit more money onto your balance?\n2. Would you like to spin the slots?\n3. Would you like to exit the game.\n\n------------------------------------------------------------\n\n> ")
    if selected_menu_option == "1":
        TOTAL_BALANCE, PERSONAL_WALLET_BALANCE = deposit(TOTAL_BALANCE, PERSONAL_WALLET_BALANCE)
    elif selected_menu_option == "2":
        configure_and_spin_slot_machine(TOTAL_BALANCE)
    elif selected_menu_option == "3":
        return selected_menu_option
    else:
        print("\nEnter a valid input.")


def main(TOTAL_BALANCE, PERSONAL_WALLET_BALANCE):
    print("\nHere is the current table of multipliers for each material: \n\n")
    for symbol, multiplier in symbol_dict.items():
        print(symbol, multiplier)
    
    while True:
        menu = action_menu(TOTAL_BALANCE, PERSONAL_WALLET_BALANCE)
        if menu == "3":
            break

    return