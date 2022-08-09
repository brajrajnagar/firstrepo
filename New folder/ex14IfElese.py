# To generate random nunmbers.
import random

def guessgame(num):
    print("Enter the integer between 0-5:", end=" ")
    input_num = int(input())
    if input_num == num :
        print("Congratulations You won. You've guessed the right number.")
    elif input_num > 5 or input_num < 0 :
        print("You've entered an invalid number.")
    else:
        print("You've guessed the wrong number. Try again?")
        guessgame(num)


n = random.randint(0,5)
guessgame(n)