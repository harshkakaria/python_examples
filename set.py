# s= {10,20,30,40}
# print(s)
# print(type(s))

# l = [10,20,30,40,10,20,30,10]
# s=set(l)
# print(s)
# # inside set duplicate not allowed and sequence doesn't matter
#

# s= set(range(5))
# print(s)

# s= {}
# print(s)
# print(type(s))
#
# s = set()
# print(s)
# print(type(s))

# Imp functions of set :
# s = {10,20,30}
# s.add(40)
# print(s)
# s= {10,20,30,40}
# l= [50,60,70,10]
# s.update(l,range(5))
# print(s)

# s = {10,20,30}
# s1=s.copy()
# print(s1)
# print(s.pop()) # remove random elements
# print(s)
# print(s.pop())
#
# s ={10,20,30}
# s.remove(30) # remove specific elements what you want,if elements not present in the set we will get keyerrors
# print(s)

# s = {10,20,30}
# s.discard(10)  # if the specific elements no present in the set then we won't get any error
# print(s)
# s.discard(50)
# print(s)

# s = {10,20,20}
# print(s)
# s.clear() # to remove all elements form the sets
# print(s)

# MATHEMATICAL OPERATIONS ON THE SET :
# 1. union()
#
# x={10,20,30,40,50}
# y={60,70,80,90}
# print(x.union(y))
# print(x|y)

# 2. intersections():

# x={10,20,30}
# y={30,40,50}
# print(x.intersection(y))
# print(x&y)

# 3.difference

# x={10,20,30,40,50}
# y={10,30,40,50,60}
# print(x.difference(y))
# print(x-y)

# 4 symmetric_difference

# x={10,20,30,40}
# y={30,40,50,60}
# print(x.symmetric_difference(y)) # not in both
#

# set compreshension:
# s={x*x for x in range(5)}
# print(s)
# note : Set object won't support indexing and slicing
# print(s[0])
# print(s[1:3])
# TypeError: 'set' object does not support indexing


# exmp :
# l = eval(input("Enter list of values:"))
# s=set(l)
# print(s)  # remove duplicate
# : Enter list of values:[10,20,30,20,10,20]
# #outputs {10, 20, 30}

# second apporach
l=eval(input('Enter list of values:'))
l1=[ ]
for x in l:
    if x not in l1:
        l1.append(x)
print(l1)









