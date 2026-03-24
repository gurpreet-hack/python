# a=(1,2,3,4,5)
# a[0]=10
# print(a)
# # ------------
# a=(1,2,3,4,5)
# print(a)
# #---------

# b=[1,2,3,4,5]
# print(type(b))
# c=tuple(b)
# print(type(c))
# ----------
# a=(1,2,3,4,5)
# print(len(a))
# --
# a=(1,2,3,4,5)
# print(type(a))
# print("tuple:")
# b=list(a)
# print(type(b))
# b[0]=10
# print(b)
# c=tuple(b)
# print(c)
#--------------
# a=(1,2,3,4,5)
# print(a)
# print(type(a))
# b=list(a)
# b.append(6)
# print(b)
# print(type(b))
# c=tuple(b)
# print(c)
# print(type(c))
# #--------------remove from tuple----------------
# a=(1,2,3,4,5)
# print(a)
# print(type(a))
# b=list(a)
# b.remove(3)
# print(b)
# print(type(b))
# c=tuple(b)
# print(c)
# print(type(c))
#--------------sort tuple----------------
# a=(15, 10, 15, 20, 25)
# b=list(a)
# b.sort()
# print(b)
# c=tuple(b)
# print(c)
# del c
# print(c)
#----------------
# a=(15, 10, 15, 20, 25)
# for i in range(len(a)):
#     print(a[i])
#------------
# a=(15, 10, 15, 20, 25)
# for i in range(len(a)):
#     if a[i]==15:
#         print(i)
# #-------
# a=(15, 10, 15, 20, 25)
# b=(1,2,3,4,5)
# c=b*2
# print(c)

# a={"a","b","c"}
# print(a)

# print(type(a))
# a=set((1,2,3,4))
# print(a)
#a={5,6,7,8}
# print(1 not in a)
# a.add(5)
# print(a)
# b={5,6,7,8}
# a.update(b)
# print(a)


# a.remove(4)
# print(a)
# a.discard(8)
# print(a)

# a={1,2,3,4}
# b={5,6,7,8}
# c=a.union(b)
# print(c)
# a={1,2,3,4}
# b={5,6,7,8}
# d={1,2,8,9,10}
# c=a|b|d
# print(c)
# print(type(c))


# a={1,2,3,4}
# b=[4,5,6]
# c=a.union(b)

# print(c)
# print(type(c))
#-------------
# a={1,2,3,4}
# b=frozenset(a)
# print(a,b)
# print(type(a),type(b))
# c=a.remove(1)
# d=b.remove(1)
# print(c,d)

# a={1,2,3,4}
# b=a.copy()
# print(b)
# del b
# print(b)

# x={"apple","banana","cherry"}
# y={"b","c","apple"}

# z=x.difference(y)
# print(z)

# x={"apple","banana","cherry"}
# y={"b","c","apple"}

# x.difference_update(y)
# print(x)

# x={"apple","banana","cherry"}
# y={"b","c","d"}

# z=x.isdisjoint(y)
# print(z)
#------------------
# x={"a","b","c","d"}
# y={"a","b","c","d","e"}
# z=x.issubset(y)
# print(z)
#---------------
# x=int(input("enter your age :"))
# y=str(input("you have voter card:"))
# a=y.upper()

# if x>=18 and a=="YES":
#     print("yes you can vote")
# elif x>=18 and a!="YES":
#     print("ypu have not voter id card")

# else:
#     print("ypu cannot vote")
#-----------------------
a=15
b=10
if a>b: print("a is greater then b")
