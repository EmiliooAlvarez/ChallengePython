print('Welcome to the Multiplication/Exponent Table App')
name=input('What is your name?: ')
print(f'Welcome to the App{name}!')


number = int(input ("Enter the number of which the user wants to print the multiplication table: "))      
# We are using "for loop" to iterate the multiplication 10 times       
print ("The Multiplication Table of: ", number)    
for count in range(1, 11):      
   print (number, 'x', count, '=', number * count)   
   number = int(input ("Enter the number of which the user wants to print the multiplication table: "))  
   break


number = int(input ("Enter the number of which the user wants to print the multiplication table: "))      
# We are using "for loop" to iterate the multiplication 10 times       
print ("The Multiplication Table of: ", number)    
for count in range(1, 11):      
   print (number, 'x', count, '=', number ** count)   
   number = int(input ("Enter the number of which the user wants to print the multiplication table: ")) 
   break