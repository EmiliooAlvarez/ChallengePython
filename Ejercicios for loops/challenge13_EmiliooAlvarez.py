print('Welcome to the Factorial Calculator App')
num=int(input('What number would you like to compute the factorial of?:'))

def fact_1(n):
    factorial_total = 1
    while n > 1:
        factorial_total *= n
        n -= 1
        print(n)
    return factorial_total
print(num)