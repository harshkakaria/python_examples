# d={}
# d[100]='jai'
# d[200]='giri'
# print(d)
# print(d[200])

# To display % and name in dicitionary and display info
# rec ={}
# n=int(input('Enter no of elements of students:'))
# i=1
# while i<=n:
#     name=input('Enter student name:')
#     marks=input('Enter student marks:')
#     rec[name]=marks
#     i += 1
# print('Name of students ','\t','% of marks')
# for x in rec:
#     print('\t',x,'\t\t', rec[x])
#

# get() function

# d={1:'jai',2:'jaya',3:'veera'}
# print(d[1])
# print(d.get(1))
# print(d.get(2))
# # print(d.pop(1))
# print(d.popitem())
# print(d)


# d={100:'jai',200:'jaya',300:'veera'}
# print(d.keys())
# for k in d.keys():
#     print(k)

# print(d.values())
# for v in d.values():
#     print(v)
#
# for k ,v in d.items():
#     print(k,'--',v)

# imp exp

# words = input("Enter any words:")
# d={}
# for x in words:
#     d[x]=d.get(x,0)+1
# for k,v in d.items():
#     print(k,'occurred' ,v, 'times')
#


#dictionary comprehension:
sq = {x:x*x for x in range(1,6)}
print(sq)
for i in sq.items():
    print(i)







































