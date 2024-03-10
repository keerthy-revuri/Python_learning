#logic 1 - using recursive function
def factorial(n):
        if n == 1:
            return 1
        return n * factorial(n-1)

res = factorial(5)
print(res)

#logic 2 - using while loop
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n ==1:
        return 1
    else:
        fact = 1
        while n > 1:
            fact = fact * n
            n=n-1
    return fact
res = factorial(6)
print(res)

#logic3 - using for loop
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n ==1:
        return 1
    else:
        fact = 1
        for i in range(2, n+1):
            fact = fact * i
        return fact
res = factorial(6)
print(res)