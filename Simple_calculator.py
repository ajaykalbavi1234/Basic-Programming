def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def division(a,b):
    return a/b
def multiplication(a,b):
    return a*b
def power(a,b):
    return a**b
def modulus(a,b):
    return a%b

num1 = int(input())
num2 = int(input())
operation = int(input())
print('1. addition \n 2. subtraction \n 3. division \n 4. multiplication \n 5. power \n 6. modulus \n')

if operation <= 6:
    if operation == 1:
        print(addition(num1,num2))
    elif operation==2:
        print(subtraction(num1,num2))
    elif operation == 3:
        print(division(num1,num2))
    elif operation == 4:
        print(multiplication(num1,num2))
    elif operation == 5:
        print(power(num1,num2))
    elif operation == 6:
        print(modulus(num1,num2))
else:
    print('Invalid Input')