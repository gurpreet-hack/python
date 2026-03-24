print("hello")
###############################################################
name="Arshita"
age=20
print("My name is",name,"and i'm",age,"years old")
################################################################
# Data Types
x="Arshita"
print(x)

x=10
print("The value of x is:",x)

x=0.1
print(x)
##############################################################
# Check Type
x=10
print(type(x))

x="A"
print(type(x))

x=0.1
print(type(x))
###############################################################
# Lists
colours=["Red","Yellow","Green","Blue"]
print(colours)
colours.append("Black")
print(colours)
##############################################################
# Tuple
fruits=("Mango","Banana","Apple")
print(fruits)
###############################################################
# Dictionary
student={
    "name":"Arshita",
    "age":20,
    "address":"hr"
}
print(student)
################################################################
# Sets
numbers={1,2,3,4}
print(numbers)
################################################################
# String manipulation
name="Python"
print(name[1])
###############################################################
# If-else
x=20
if x<=30:
    print("true")
else:
    print("false")
##################################################################
# For loop
for i in range(5):
    print(i)
################################################################
# Operators
a=20
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
##################################################################
# Diff. Methods to print instead of print()
import sys
sys.stdout.write("hello")

from pprint import pprint
pprint('hello')

import logging
logging.warning("Hello")

##################################################################
# Find the no. is odd or even
x=10
if x%2==0:
    print("Even")
else:
    print("Odd")
#################################################################
# Find the no. is positive or negative
x=-20
if x>=0:
    print("Positive")
else:
    print("Negative")
#################################################################
# Find which no. is greater
x=5
y=9
if x>y:
    print("5 is greater")
else:
    print("9 is greater")
#################################################################
# Check if candidate is eligible to vote or not
x=16
if x>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
##################################################################
# Check if student is pass or fail
x=60
if x>=40:
    print("Pass")
else:
    print("Fail")
####################################################################
# Loop from 1 to 10
for i in range(1,11):
    print(i)
####################################################################
# Loop the Even Numbers
for i in range(1,21):
    if(i%2==0):
        print(i)
#####################################################################
# Loop the string
name="Python"
for n in name:
    print(n)
####################################################################
# Square of numbers
numbers=[1,2,3,4,5,6,7,8,9,10]
for num in numbers:
    print(num*num)
###################################################################
# Star pattern
for i in range(0,6):
    print("*"*i)
###################################################################
# Check Number is positive, negative or zero.
x=0
if x>0:
    print("Positive")
elif x<0:
    print("Negative")
else:
    print("Zero")
#######################################################################
# Reverse Numbers
for i in range(10,0,-1):
    print(i)
#####################################################################
# Sum of numbers 1 to 10
total=0
for i in range(1,11):
    total=total+i
print(total)
#######################################################################
# Count even numbers between 1 and 20
count=0
for i in range(1,21):
    if i%2==0:
        count=count+1
print(count)
######################################################################
# Reverse star pattern
for i in range(5,0,-1):
    print("*"*i)
#####################################################################
# Print characters with index
name="Python"
for i in range(len(name)):
    print(name[i],i)
####################################################################
# Print number pattern
for i in range(1,6):
    print(str(i)*i)