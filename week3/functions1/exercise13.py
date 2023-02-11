import random
def game():
    print("Hello! What is your name?")
    name = input()
    print("Well, ", name, ", I am thinking of a number between 1 and 20", sep="")
    x = random.randint(1, 20)
    print("Take a guess.")
    cnt = 0
    num = 0
    while num!=x:
        num = int(input())
        if num>20 or num<1:
            print("Please enter number in range 1 to 20")
        elif num<x:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        cnt += 1
    print("Good job, ", name, "! You guessed my number in ", cnt, " guesses!", sep="")