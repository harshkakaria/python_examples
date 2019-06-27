# s= 'jaigiri'
# print(len(s))

# s = input("Enter main strings:")
# subs = input("Enter sub strings:")
# if subs in s:
#     print(subs,'is found in main strings')
# else:
#     print(subs,'is not found in main strings')

# counting substrings in the given strings
# s= 'abababababcababcacadada'
# print(s.count('a'))
# print(s.count('ab'))
# print(s.count('a',3,7))

# Nested list as matrix
# n=[[10,20,30],[40,50,60],[70,80,90]]
# print(n)
# print("Enter elements by row size:")
# for r in n:
#     print(r)
#
# print("Elements by matrix style:")
# for i in range(len(n)):
#     for j in range(len(n[i])):
#         print(n[i][j],end=' ')
#     print()


# list comprehensions:
# s= [x*x for x in range(1,11)]
# print(s)
# v= [2**x for x in range(1,6)]
# print(v)
# m= [x for x in s if x%2==0]
# print(m)
#
# words = ['banana','apple','balck','blue']
# l= [w[0] for w in words]
# print(l)

# write a program to display unique vowels present in the given words

# vowels = ['a','e','i','o','u']
# word =input("Enter the word to search for vowels:")
# found =[]
# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)
# print(found)
# print("The num of different vowels present in ",word,'is',len(found))