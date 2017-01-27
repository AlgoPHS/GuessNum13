# Guess a number 13
# Algo 2017
# Marie + Tyler 
import random
def playGame():
    number = random.randint(1,101)
    tries =0
    while True:
        print("What is your guess?")
        guess = int(input())
        tries+=1
        if guess == number:
            print("Well done. I'm so proud!")
            print("The number was " + str(number))
            print("It took you %s tries."%(tries))
            break
        if guess > number:
            print("Too high, try again!")
        if guess < number:
            print("Too low, try again!")
        
def main():
    print("I have a number between 1 and 100.")
    playGame()
    games =1
    while True:
        print("You played %s games"%(games))
        print("Would you like to play again? (y/n)")
        answer = input()
        if answer == 'y':
            games +=1
            playGame()
        else:
            break
main()
