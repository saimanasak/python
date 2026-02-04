#To use random method we need to import random:
import random

#Colors class to define all the colors and code:
#Here, ANSI escape codes are used:
class colors:
    Red = '\033[31m'
    End = '\033[m'
    Cyan = '\033[36m'
    Yellow = '\033[33m'
    Green = '\033[32m'
    Blue = '\033[34m'
    Purple = '\033[35m'
    
MAX_GUESSES = 10

def guessing_game():
    
    #Introduction to game:
    print(colors.Purple + "                             ****** Welcome to Guessing Game ******                       ", colors.End)
    print(colors.Purple + """
          
          You need to guess a number, which is randomly generated.
          In the first turn: if your guess is within the range of 10 to the actual number --> WARM
                             if your guess is farther from the actual number --> COLD
          In the remaining turns: if your guess is closer to the actual number than the previous guess --> WARMER
                                  if your guess is farther from the actual number than the previous guess --> COLDER
          If your guess out of the range [1,100] --> OUT OF BOUND 
          
          
          Here, you go......CHECK YOUR LUCK ;) 
          
          
          """, colors.End)
    
    #Guess, count and guessed_array are initialized and declared:
    guess = int(input("Guess a number: "))
    guessed = []
    count = 0
    
    #Random number is generated and stored in number variable:
    number = random.randint(1, 100)
    
    #Prints the random number: for testing purpose
    #print(number)
    
    #First turn of guess:
    if count == 0 and (guess < 1 or guess > 100):
        print(colors.Red + "OUT OF BOUND! guess again...\n", colors.End)
        count = count + 1
        guessed.append(guess)
        
    elif count == 0 and 10 > abs(guess - number):
        print(colors.Blue + "WARM! guess again...\n", colors.End)
        count = count + 1
        guessed.append(guess)
        
    elif count == 0 and 10 < abs(guess - number):
        print(colors.Yellow + "COLD! guess again...\n", colors.End)
        count = count + 1
        guessed.append(guess)
            
    #For all subsequent turns:
    while guess != number and count < MAX_GUESSES:
        
        guess = int(input("Guess a number: "))
        
        if guess < 1 or guess > 100:
            print(colors.Red + "OUT OF BOUND! guess again...\n", colors.End)
            count = count + 1
            guessed.append(guess)
        
        elif (abs(guess - number) < abs(guessed[-1] - number)):
            print(colors.Blue + "WARMER! guess again...\n", colors.End)
            count = count + 1
            guessed.append(guess)   
            
        elif (abs(guess - number) > abs(guessed[-1] - number)):
            print(colors.Yellow + "COLDER! guess again...\n", colors.End)
            count = count + 1
            guessed.append(guess)  
            
        elif guess == number:
            break
        
        print(f"Attempts left: {MAX_GUESSES - count}\n")
    
    # Print the game statistics
    if guess == number:
        print(colors.Green + "Congrats! your guess is CORRECT :) \n", colors.End)
        print(colors.Cyan + "No.of guesses:", colors.End, "{}".format(count))
        print(colors.Cyan + "Guessed numbers:", colors.End, "{} \n".format(guessed))
    else:
        print(colors.Red + "Game Over! You've used all your guesses.\n", colors.End)
        print(colors.Cyan + "Guessed numbers:", colors.End, "{} \n".format(guessed))
        print(colors.Cyan + "The correct number was:", colors.End, number)

guessing_game()