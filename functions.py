def wish():
    print("hello this is user define function")

wish()
wish()

def wish(name):
    print("hello",name,'good morning')

wish('jai')
wish('veera')

# Return statements:
def add(x,y):
    return x+y
result = add(1,20)
print('the sum of :',result)
print('the sum of ',add(20,40))


def f1():
    print('hello')
f1()
print(type(f1()))

# to check given no is odd or even
def even_or_odd(num):
    if num%2==0:
        print(num,'is even no')
    else:
        print(num,'is odd num')

even_or_odd(11)
even_or_odd(12)

# find factorial of given no:
def fact(num):
    result = 1
    while num >= 1:
        # result = result * num
        result *=num
        # num = num - 1
        num -= 1
    return result

for i in range(1, 6):
    print("the factorial of ", i, 'is:', fact(i))
print(fact(5))

# returning multiple values from a functions
def sum_math(a,b):
    sum=a+b
    diff=a-b
    # mul=a*b
    # mod=a%b
    # flor=a//b
    return sum,diff
x,y=sum_math(10,20)
print("the sum ",x,y,sep='\n')

def cal(a,b):
    sum = a + b
    diff=a-b
    mul=a*b
    mod=a%b
    flor=a//b
    return sum,diff, mul,mod,flor

t=cal(30,20)
print('The result is:')

for i in t:
    print(i)

# Positional args:
def sub(a,b):
    print(a-b)

sub(10,20)
sub(20,10)

# keywords args:

def wish(name,msg):
    print('hello ',name,msg)

wish(name='jai',msg='good eve')
wish(msg='good ene',name='jai')


def sum(*n):
    total =0
    for n1  in n:
        total =total+n1
        print('the sum is:',total)


sum()
sum(1)
sum(1,2)
sum(1,2,3,4)

def display(**kwargs):
    for k,v in kwargs.items():
        print(k,'=' ,v)

display(n1=1,n2=2,n3=4)
display(rno=100,name='durga',marks=90)



# types of variables:
a=10   # global variable
def f1():
    print(a)

def f2():
    print(a)

f1()
f2()

def f1():
    a=10 # local variable
    print(a)

def f2():
    print(a)

f1()
f2()
# without global keywords
a=10
def f1():
    a=77
    print(a)

def f2():
    print(a)

f1()
f2()

# global keywords
a=10
def f1():
    global a
    a=77
    print(a)

def f2():
    print(a)
f1()
f2()

# note : using global keywords to declare global variable inside function

a=10 # global variable
def f1():
    a=77 # local variable
    print(a)
    print(globals()['a']) # print for global variable

f1()

def fact(n):
    if n==0:
        result =1
    else:
        result =n*fact(n-1)
    return result

f=int(input("Enter any no:"))
print('Factorial of {} is = {}'.format(f,fact(f)))


def decor(fun):
    def inner(name):
        if name=="sunny":
            print('hello sunny bad morning')
        else:
            fun(name)
    return inner

@decor
def wish(name):
    print('hello ',name,'good morning')

wish('jaya')
wish('jai')
wish('veera')
wish('sunny')

def decor(fun):
    def inner(name):
        if name =='jai':
            print('hello jai bad morning ')
        else:
            fun(name)
    return inner

def wish(name):
    print('hello ',name,'good evening')

decorfunction = decor(wish)

wish('jaya')
wish('maya')

decorfunction('jaya')
decorfunction('maya')
decorfunction('jai')

def decor(func):
    def inner(name):
        print('first decor (decor) function exe')
        func(name)

    return inner

def decor1(func):
    def inner(name):
        print('second decor (decor1) exe')
        func(name)
    return inner


@decor1
# @decor
def wish(name):
    print('hello', name, 'good morning')


wish('jaya')
