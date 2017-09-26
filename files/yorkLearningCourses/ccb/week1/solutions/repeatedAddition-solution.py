"""Performs Multiplication of two numbers by repated addition """

num1 = int(input("First Number "))
num2 = int(input("Second Number "))
result = 0

while num2 > 0: #This works, but a for loop would be cleaner
    result += num1
    num2 -= 1

print("Result = " + str(result))
