# a=(1,2,3,4)
# # a[0]=2
# print(a)

#----> Print tuple
a=(1,2,3)
print(a)

#----> Change list to tuple
a=[1,2,3,4,5]
print(type(a))
b=tuple(a)
print(type(b))

#---> Length of a tuple
a=(5,6,7,8)
print(len(a))

#---> Add element to tuple but using casting
a=(0,1,4,7)
b=list(a)
b.append(10)
c=tuple(b)
print(c)

#---> Repitition in tuple
a=(1,2,3)
b=a*2
print(b)

#---> Count
a=(1,2,3,4,5,7,8,1,2,3)
b=a.count(2)
print(b)

#---> Index
a=(2,3,4,5,2,7,8)
b=a.index(2)
print(b)

#---> Loop
a=(5,6,7,8,9)
for i in range(len(a)):
    print(a[i])

#---> Concat
a=(1,2,3)
b=(4,5,6)
c=a+b
print(c)

#---> Min, Max, Sum
a=(1,2,3)
print(max(a))
print(min(a))
print(sum(a))

#---> Membership Check
a=(1,2,3,4)
if 2 in a:
    print("true")
else:
    print("false")

#---> Slicing
a=(4,5,6,7)
print(a[1:3])