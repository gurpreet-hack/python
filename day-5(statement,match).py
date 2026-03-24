#---> Input
x=int(input("enter your age:"))
print(x)

#---> If, elif, else statement
x=int(input("Enter your age:")) 
y=str(input("have voter card ? :"))
a=y.upper()
if x>=18 and a=="YES":  
    print("eligible to vote")
elif a!="YES":
    print("Can't Vote")
else:
    print(" not Eligible to vote")

#---> Shorthand
a=5
b=2
if a>b: print("a is greater than b")

#OR
a=10
b=50
bigger=a if a>b else b
print("the big element is :",bigger)

#OR
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#---> Logical Operators
a=10
b=20
c=30
if b<c and a<b:
   print("A")
if a>c or c>a:
   print("B")
if not a>c:
   print("C")

#---> Nested if statement
x=15
if x>10:
    print("yes")
    if x>20:
        print("yes it is greater then 20")
    else:
        print("ofoo")
    if x>40:
        print("win")

#---> Match statement
day = 7
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case _:
    print("Sunday")

# OR
day=6
match day:
   case 1|2|3|4|5:
      print("Today is a weekday")
   case 6|7:
      print("I love weekends!")