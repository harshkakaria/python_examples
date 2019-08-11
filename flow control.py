# if statements

name=input('enter name:')
if name=="jai":
    print('helloo jai')
print('how are you!!!')

# if elif else
while True:
    brand = input("Enter your fav brand:")
    if brand == 'rc':
        print("it's children collections")
    elif brand == 'kf':
        print('it is old colle')
    elif brand == 'fo':
        print('buy one get one free')
    else:
        print('other brand are not recommended')

n=int(input("Enter any no:"))
if n >=1 and n<=10:
    print('The no ',n,'is in between 1 to 10')
else:
    print('The no',n,'is not in between 1 to 10')

s = input("Enter some strings:")
i=0
for x in s:
    print("The character present at",i,"index is:",x)
    i=i+1

for x in range(10,0):
    print(x)

# nested loops:
for i in range(4):
    for j in range(6):
        print('i=',i, 'j=',j)

# Write a program to display *'s in Right angled triangled form
n =int(input("Enter no of rows:"))
for i in range (1,n+1):
    for j in range(1,i+1):
        print("*" ,end =' ')
    print()

# alternative way to display *'s

n=int(input("Enter no of rows:"))
for i in range (1,n+1):
    print(""*(n+1),end=' ')
    print('*'*i)

# Equivalent triangle display
n=int(input("Enter any no of rows :"))
for i in range(1,n+1):
    print(' '* (n-i),end='')
    print('* '*i)

# Break statements and continue

for i in range(10):
    if i==7:
        print('Processing is enough pls break...')
        continue
        # break
    print(i)

for i in range(10):
    if i%2==0:
        continue
    print(i)

cart = [10,20,400,499,500,700,50,60]
for item in cart:
    if item >=500:
        print("We can't process this item:",item)
        continue
    print(item)

numbers = [10,20,30,40,50,0,5,300]
for n in numbers:
    if n==0:
        print('hey how we can divide with zero ..just skipping')
        continue
    print('100/{}={} '.format(n,100/n))



cart =[10,20,30,499,500,40,50]
for item in cart:
    if item >= 500:
        print('We can not process this item')
        break
    print(item)
else:
    print('congrts...all items processed successfully...')

#  pass statement
for i in range(100):
    if i%9==0:
        print(i)
    else:
        pass


s ='Learning python is very easy!!!'
n=len(s)
i = 0
print('forward directions')
while i<n:
    print(s[i],end='')
    i = i+1





