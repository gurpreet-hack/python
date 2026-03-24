# Print variable as well as words, addition, multiplication
print(5)
x=5
print(x)
print(3*3)
print(3+3)
x=35
print("my age is ",x,"and i am male")

# Casting
x=5
y=int(x)
z=str(x)
c=float(x)
d=complex(x)
print(x,y,z,c,d)

# Assign values to the variables in one line
x="a"
y="b"
z="c"
x,y,z="a","b","c"
print(x,y,z)

# Unpack one list into variables
fruits=["orange","apple","mango"]
a,b,c=fruits
print(a,b,c)

# Assign same value to multiple variables
a=b=c="orange"
print(a,b,c)

# Concat (+) and separate (,)
x="my"
y="name is"
z="Aryan"
print(x,y,z)
print(x+y+z)

# Global variables
x=5
def fun(x):
    print(x)

fun(x)

# Boolean
x=0
y=bool(x)
print(y)
print(type(y))

# Data Types (int, float, complex)
x=5
y=int(x)
z=float(y)
a=complex(z)
print(x,y,z,a)

# Slicing
a="my name is arshita rana"
print(a)
print(a[0:-1])


# Sets
#----> To add
a={1,2,3,4}
a.add(5)
print(a) 

#----> Another method to write set
a=set((4,5,6,7))
print(a)

#----> Type cast list to set
x=[0,1,3,5]
print(type(x))
print(x)
y=set(x)
print(type(y))
print(y)

#----> To update
a={1,2,3}
b={4,5,6}
b.update(a)
print(b)

#---> To remove
a={5,6,7,8,9}
a.remove(6)
print(a)

#---> Discard
a={1,3,5,7}
a.discard(3)
print(a)

#---> Delete (Delete whole set)
a={2,4,6,8}
# del a
print(a)

#---> Pop (removes the first element in a set)
a={1,2,3,4,45}
a.pop()

#---> Union (join set to set, set to tuple, set to list)
a={1,2,3,4}
b={5,6,7,8}
d={9,1,2,3,4}
c=a | b | d
c=a.union(b,d)
print(c)

a={1,2,3,4,5}
b=[6,7,8,9]
c=a.union(b)
print(c)
print(type(c))

#---> Frozen set (it doesn't allow to do changes in a set)
a={1,2,3,4,5}
b=frozenset(a)
print(b)
a.remove(1)


#---> Copy (it copies the data from another set)
c=a.copy()
print(c)

#---> Clear (used to clear elements of set but not the whole set)
a.clear()
print(a)

#---> Difference (returns the elements of set a which are not present in set b)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=x.difference(y)
print(z)

#---> Difference_update (removes the similar element of set b from set a)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

# ---> Intersection (returns the common elements if set a and set b)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=x.intersection(y)
print(z)

#---> Intersection_update( removes the other elements from set which are not similar to other set)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#---> isdisjoint() (it returns true if no element of set a is present in set b)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=x.isdisjoint(y)
print(z)

#---> issubset() (returns true if all elements of set a are present in set b)
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

#---> issuperset() (returns true if all elements of set b are present in set a)
x = {"a", "b", "c"}
y = {"f", "e", "d", "a", "b", "c"}
z = x.issuperset(y)
print(z)


#---> Symmetric difference (returns all elements of both set excluding common elements)
x={"cherry","mango","apple"}
y={"banana","apple","peach"}
z=x.symmetric_difference(y)
print(z)

#---> Symmetric difference update (removes the common element remaining print)
x={"cherry","mango","apple"}
y={"banana","apple","peach"}
x.symmetric_difference_update(y)
print(x)