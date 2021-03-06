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

# A simple program to get the current date in yymmdd format
import datetime as DT
d1 = DT.datetime.now().strftime('%y-%m-%d').replace('-','')
d1

# An extension of the above program to get the difference in dates
d2 = (DT.datetime.now().day)
d3 = (DT.datetime.now().day-DT.timedelta(2).days)
print(d2-d3)

#An additional extension where the above program is shown difference in seconds
print(DT.datetime.now().second-DT.timedelta(5).seconds)