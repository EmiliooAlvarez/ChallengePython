print('Welcome to the Binary/Hexadecimal Converter App')
num=int(input('Compute binary and hexadecimal values up to the following decimal number: '))
num2=1
lista=[]
print('Generating lists.....Complete!')
lista.append(num)
listab=[]
print('Using slides we will now show a portion of each list.')
a=int(input('What decinal number would you like to start at:'))
b=int(input('What decimal number would you like to start at:'))
listab.append(a)
listab.append(b)
print(f'Decimals values from {a} to {b}:')
x=range(a,round(float(b)+1))
for num in x:
    print(num)

print(f'Binary values from {a} to {b}: ')

h=range(a,round(float(b)+1))
for num in h:
    print(bin(num))

print(f'Hexadecimal values from {a} to {b}:')
j=range(a,round(float(b)+1))
for num in j:
    print(hex(num))

print(f'Press ENTER to see all values from {num2} to {num}: ')
print('Decimal---Binary---Hexadecimal')
print('-----------------------------')

x=range(a,round(float(b)+1))
for num in x:
    print(num)
h=range(a,round(float(b)+1))
for num in h:
    print(bin(num))
j=range(a,round(float(b)+1))
for num in j:
    print(hex(num))