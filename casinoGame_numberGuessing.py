import random

from insult_generator import insult_picker

def get_random_number():
    while True:
        try:
            beginRange = int(input("\nEnter an integer at which you would like the range to begin:\n\n"))
            endRange =  int(input("\nEnter an integer at which you would like the range to end:\n\n"))
            randNumber = random.randrange(beginRange, endRange)
            return randNumber, beginRange, endRange
        except:
            insult = insult_picker()
            print("\nYou entered an invalid input, stop being a " + insult + " and try again.")

def main():
    print("\nWelcome to the number guessing game.\nYou will pick a range, among which I will choose a random number.\nYou must guess the number I have chosen in the least number of attempts, and the only feedback I will give is wheather you are too high or too low.")
    willToContinue = "nr"
    highScore = None  
    lastBeginRange, lastEndRange = None, None  

    while True:  
        if willToContinue == "nr":  
            randNumber, beginRange, endRange = get_random_number()

            if (lastBeginRange, lastEndRange) != (beginRange, endRange):
                highScore = None  

            lastBeginRange, lastEndRange = beginRange, endRange  

        score = 0
        print("\nThe range which you selected is: " + str(beginRange) + "-" + str(endRange))
        guessCorrect = False

        while not guessCorrect:
            try: 
                insult = insult_picker()
                score += 1
                user_input = input("\n________________________________________________________________________________________\n\nPick your number you " + insult + " :\n\n= ")

                if user_input.lower() == "exit":
                    print("\nQuitting game. Your final high score was:", highScore if highScore else "No high score set.")
                    return

                guess = int(user_input)  

                if guess == randNumber:
                    if highScore is None or score < highScore:
                        highScore = score
                    print("\nYou have guessed correctly! Congratulations, you are spending your time putting numbers into a programme, is your money right, is your glock cocked to the top, if not then think again")
                    print("\n________________________________________________________________________________________\n\nYour score for this round was: " + str(score))
                    print("Your high score for this game is: " + str(highScore))
                    guessCorrect = True
                elif guess < randNumber:
                    print("\nYour guess is too low you " + insult + " , try again.")
                elif guess > randNumber:
                    print("\nYour guess is too high you " + insult + " , try again.")

            except ValueError:
                insult = insult_picker()
                print("\nYou have entered an invalid input, why are you such a " + insult + " , TRY AGAIN!")

        willToContinue = input("\n________________________________________________________________________________________\n\nWould you like to:\n"
                               "1. Keep the current range and continue (Enter 'y')\n"
                               "2. Pick a new range (Enter 'nr')\n"
                               "3. Quit the game (Enter anything else)\n\n").lower()
        
        if willToContinue == "y":
            randNumber = random.randint(beginRange, endRange)  
        elif willToContinue != "nr":  
            print("\nThanks for playing, loser! Your final high score was:", highScore if highScore else "No high score set.")
            return
