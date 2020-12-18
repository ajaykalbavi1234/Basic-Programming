#First command in the program

print('Hello World!!!')

#Second command in the program

lst = []
for i in range(1,10):
    lst.append(int(input()))
print(lst)


#A simple function to find the factorial of a given number
def Factorial(n):
    fact = 1
    for j in range(1,n+1):
        fact = fact*j
    return fact

print(Factorial(int(input())))

# A simple function to perform Recursion
# We can also perform the above mentioned factorial function as follows
def Factorial_new(n):
    if n > 0:
        if n == 1:
            return 1
        else:
            return (n*Factorial_new(n-1))
    else:
        return 1
print(Factorial_new(int(input())))
