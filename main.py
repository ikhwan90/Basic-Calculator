'''
Basic calculator for adding, subtracting, multiplying, dividing, and power
the output will be in integer
'''

import math


x = int(input('first number: '))
y = int(input('second number: '))

z = input('input the arithmetic operator or statement(+,-,*,/,**) : ')

a = '+'
b = '-'
c = '*'
d = '/'
e = '**'

if z == a:
    print(x + y)
elif z == b:
    print(x - y)
elif z == c:
    print(x * y)
elif z == d:
    print(int(x / y))
elif z == e:
    print(int(math.pow(x, y)))
else:
    print('invalid operator entered !')







