from math import factorial
print('Welcome to the Factorial Calculator App')
num=int(input('What number would you like to compute the factorial of?:'))

for x in range(1,num+1):
    print(f'{num}! ==end''' )

def factorial(num): 
    if num < 0: 
        print("Factorial of negative num does not exist")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 


print("Factorial of",num,"is", factorial(num)) 

