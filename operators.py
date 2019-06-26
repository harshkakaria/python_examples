# Python
# 3.6
# .6(v3
# .6
# .6: 4
# cf1f54eb7, Jun
# 27
# 2018, 03: 37:03) [MSC v.1900 64 bit(AMD64)]
# on
# win32
# Type
# "copyright", "credits" or "license()"
# for more information.
#     >> > '''Operators'''
# 'Operators'
# >> > a = 10
# >> > b = 20
# >> > print('a+b=', a + b)
# a + b = 30
# >> > print('a-b=', a - b)
# a - b = -10
# >> > print(a * b)
# 200
# >> > print(a % b)
# 10
# >> > a = 20
# >> > b = 10
# >> > print(a % b)
# 0
# >> > print(a // b)
# 2
# >> > print(a ** b)
# 10240000000000
# >> > '''relational operators'''
# 'relational operators'
# >> > a = 10
# >> > b = 20
# >> > print(a > b)
# False
# >> > print(a >= b)
# False
# >> > print(a < b)
# True
# >> > '''identity operator'''
# 'identity operator'
# >> > ''' is is not'''
# ' is is not'
# >> > a = 10
# >> > b = 20
# >> > print(a is b)
# False
# >> > print(a is not b)
# True
# >> > '''membership operator'''
# 'membership operator'
# >> > x = 'hello world '
# >> > print('h' in x)
# True
# >> > print('e' not in x)
# False
# >> > print('l' not in x)
# False
# >> > '''math module'''
# 'math module'
# >> > import math
# >> > print(math.sqrt(16))
# 4.0
# >> > print(math.pi)
# 3.141592653589793
# >> > import math as m
# >> > print(m.sqrt(16))
# 4.0
# >> > from math import sqrt
# >> > from math import sqrt, pi
# >> > print(pi)
# 3.141592653589793
# >> > import math *
# SyntaxError: invalid
# syntax
# >> > import math *
# SyntaxError: invalid
# syntax
# >> > x = 1110.00
# >> > print(ceil(x))
# Traceback(most
# recent
# call
# last):
# File
# "<pyshell#41>", line
# 1, in < module >
# print(ceil(x))
# NameError: name
# 'ceil' is not defined
# >> > '''read multiple value in single lines'''
# 'read multiple value in single lines'
# >> > a, b = [int(x) for x in input('Enter any no:').split()]
# Enter
# any
# no: 11
# 111
# >> > a
# 11
# >> > b
# 111
# >> > a, b, c = [float(x) for x in input('Enter any no:).split(', ')]


# cmd line args
# x = eval(input("enter any data types:"))
# from sys import argv
# print('the no of the cmd line args :',len(argv))
# print('the list of cmd line args L',argv)
# print('command line arguments one by one:')
# for x in argv:
#     print(x)

# from sys import argv
#
# sum = 0
# args = argv[1:]
# for x in args:
#     n = int(x)
#     sum += n
# print("the sum :", sum,argv)

# from sys import argv
# print(argv[1])

from sys import argv
print(argv[1]+argv[2])
print(int(argv[1])+int(argv[2]))
