'''
The Challenge:
Write a program that picks a random integer from 1 to 100, and has players guess the number.
'''

import random

num=random.randint(1, 100)
# print(f'Random number is {num}')

print('-------------WELCOME TO GUESSING GAME----------------')
print('\n')
print('1? 2 ? 3 ? 4? 5? 7? 8? 9? 10?')
print('...............45? 42 ? 43 ? 54? 65? 77? 88? 59? 60?')
print('55? 62 ? 73 ?........... 66? 65? 68? 72? 74?')
print('73? 74? 75?............94? 96? 85? 88? 99? 100?')
print('\n')

# Instruction of the Guessing Game 
print('------------------Instructions------------------')
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're 'COLD'")
print("If your guess is within 10 of my number, I'll tell you you're 'WARM'")
print("If your guess is farther than your most recent guess, I'll say you're getting 'COLDER'")
print("If your guess is closer than your most recent guess, I'll say you're getting 'WARMER'")
print("LET'S PLAY!")
print('\n')

# list to store guesses
guesses = [0]

# while loop that compares the player's guess to our number. If the player guesses correctly, break from the loop. Otherwise, tell the player if they're warmer or colder, and continue asking for guesses.¶
while True:
    try:
        guess = int(input('What is your guess?  '))
        
        # OUT OF BOUNDS!! if guess is less than 1 or greater than 100 
        if guess < 1 or guess > 100:
            print('Out of bounds! Please try again: ') 
            continue
        
        # Check if guess is equal to num 
        if guess == num:
            # Check the winning level on the basis of  length of guesses
            if len(guesses) <= 5:
                print(f'Excellent!!!\nCONGRATULATIONS! You guessed it in only {len(guesses)} guesses.')
                break
                
            if len(guesses) > 5  and len(guesses) <= 10:
                print(f'very good!!\nCONGRATULATIONS! You guessed it in only {len(guesses)} guesses.')
                break

            if len(guesses) > 10 and len(guesses) <=20 :
                print(f'Good!!\nCONGRATULATIONS! You guessed it in only {len(guesses)} guesses.')
                break

            else:
                print(f'Play well! All the best for the next time.\nYou guessed it in {len(guesses)} guesses.')       
                break

        # if guess is incorrect, add guess in list
        guesses.append(guess)
        
        # After append all new guesses to the list,we compare the new guess from previous guess, & here previous guess is given as guesses[-2]
        if guesses[-2]:
            if abs(num-guess) < abs(num- guesses[-2]):
                print('WARMER')

            else:
                print('COLDER')

        else:
            if abs(num-guess) <= 10:
                print('WARM')
            else:
                print('COLD')  

    except Exception as e:
        print('Please enter a valid number !!')    
        



