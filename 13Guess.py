import random
def main():
    number = random.randint(1,100)
    tries =0
    while True:
        if tries<4:
            print("What is your guess?")
            guess = int(input())
            tries+=1
            if guess == number:
                print("Well done. I'm so proud!")
                print("%s %s" % ("The number was", number))
                print("Would you like to play again?")
                if input() == "n":
                    break
                else:
                    number = random.randint(1,100)
                    tries = 0
            if guess > number:
                print("Too high, try again!")
            if guess < number:
                print("Too low, try again!")
        else:
            print("You have failed 4 times. Sad!")
            print("%s %s" % ("The number was", number))
            break
main()
