""" Quizzes the user on multiplication """
import random

num1 = random.randrange(1,10)
num2 = random.randrange(1,10)

guess = int(input("What is " + str(num1) + " * " + str(num2) + "? "))

if guess == num1 * num2:
    print("Correct")
else:
    print("Wrong")
