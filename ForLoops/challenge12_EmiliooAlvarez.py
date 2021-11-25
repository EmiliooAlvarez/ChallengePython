from math import sqrt
print('Welcome to the Quadratic Equation Solver App!')

print('A Quadratic equation is of the form ax^2 +bx + c = 0')
print('Your solutions can be real or complex numbers.')
print('Acomplex number has two parts: a +bj')
print('Where a is the real portion and bj is the imaginary portion.')
nume=int(input('How many equations would youlike to solve today:'))


a = float(input('Please enter your value of  a(coefficient of x^2): '))

b = float(input('Please enter your value of b(coefficient of x): '))

c = float(input('Please enter the value of c( coefficient of c): '))

if a != 0:

    discriminante= b**2 - 4*a*c

    if discriminante >=0:

        x1 = (-b + sqrt(discriminante)) / (2 * a)

        x2 = (-b - sqrt(discriminante)) / (2 * a)

        if x1==x2:

            print ('The solution of the equation is: x1=%4.3f'% x1)

        else:

            print ('Solutions of the equation: x1=%4.3f y x2=%4.3f ' % (x1, x2)  )

    else:

        print ('There is no real solutions. ')

else:

    if b != 0:

       x = -c / b

       print ('Solution of the equation : x=%4.3f ' % x)

    else:

       if c != 0:

          print ('The equation has no solution. ')

       else:

          print ('The ecuation has infinite solutions  ')
    