import random
number = random.randint(1,100)
def main():
    tries =0
    while True:
        print("What is your guess?")
        guess = int(input())
        tries+=1
        if tries<4:
            if guess == number:
                print("Well done. I'm so proud!")
                print("%s %s" % ("The number was", number))
                break
            if guess > number:
                print("Too high, try again!")
            if guess < number:
                print("Too low, try again!")
        else:
            print("You have failed 4 times. Sad!")
            print("%s %s" % ("The number was", number))
            break
main()
