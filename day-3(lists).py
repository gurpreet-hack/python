# Lists
#---> Print all elements of list using loop
a=[1,2,3,34,5,1]
print(a)
for i in range(len(a)):
    print(a[i])

#---> Convert tuple to list
b=(1,2,3,4)
c=list(b)
print(c)
print(type(c))

#---> Append (used to add element in end of the list)
a=[1,2,3,4]
a.append(12)
print(a)

#---> Extend (used to add elements of list to the current list in the end)
a=[5,6,7]
b=[1,2,3,4]
a.extend(b)
print(a)

#---> Remove(used to remove the first element of a specified value from a list)
a=[1,2,3,1,4,5]
a.remove(1)
print(a)

#---> Reverse (reverse the order of a list)
a=[1,2,3,4,5]
a.reverse()
print(a)

#---> Sort (sort the list)
a=[4,6,8,1,3,9]
a.sort()
print(a)

#---> Insert (add an element to the specified position)
a=[5,6,7,8,9]
a.insert(0,4)
print(a)

#---> Sort reverse (like descending order)
a=[4,3,2,1,5]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

#---> Clear (clears all element from a list)
a=[1,2,3]
a.clear()
print(a)

#---> Count (it count the no. elements of specified value)
a=[1,2,3,4,5,6,71,2,1,3,58,1]
b=a.count(1)
print(b)

#---> Index (returns the index position of a specified value)
a=["cherry","mango","apple"]
b=a.index("mango")
print(b)

#---> Pop (rmeoves element of a specified position)
a=["cherry","mango","apple"]
a.pop(2)
print(a)

# a=(10,[20,[30,50],60])
# x=list(a)
# b=x[1]
# print(b)
# c=b[1]
# print(c)
# c[1]=500
# print(c)
# print(x)