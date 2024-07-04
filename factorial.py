def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(1))

def myFactorial(num):
    if num<0:
        return 0
    elif num==0 or num==1:
        return 1
    else:
        fact = 1
        while(num > 1):
            fact*=num
            num-=1
        return fact
print(myFactorial(5))