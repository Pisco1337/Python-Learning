from logging import shutdown
from tracemalloc import stop


num1= float(input("Please enter the 1st number : "))
num2= float(input("Please Enter the 2nd number : "))
operation = input("Please enter the operation you want to do : ")
def sub(num1, num2):
    return num1-num2
def mlt(num1, num2):
    return num1*num2
def div(num1, num2):
    return num1/num2
def sum(num1, num2):
    return num1+num2
    
if operation == "+":
    print(sum(num1, num2))
elif operation == "-":
    print(sub(num1, num2))
elif operation == "/" and num2 == 0:
    print("You can't divide by zero")
elif operation == "/" and num2 != 0:
    print(div(num1, num2))
elif operation == "*":
    print(mlt(num1, num2))
else: print(operation+" is not a valid operator, Please enter a valid one.")
