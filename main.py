'''
Basic calculator for adding, subtracting, multiplying, and dividing
the output will be in integer
'''

x = input('first number: ')
y = input('second number: ')

z = input('input the arithmetic operator (+,-,*,/) : ')

a = '+'
b = '-'
c = '*'
d = ':'

if z == a:
    print(int(int(x) + int(y)))
elif z == b:
    print(int(int(x) - int(y)))
elif z == c:
    print(int(int(x) * int(y)))
elif z == d:
    print(int(int(x) / int(y)))
else:
    print('error !')








