# While Loop
i=1
while (i<=6):
    print(i)
    i=i+1

# Break statement
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1

# Continue statement
i=0
while(i<=7):
    
    i=i+1
    if i==3:
        continue
    print(i)

# Else statement
i=1
while i<6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6")

# Multiple conditions
x=0
y=10
while x<5 and y>5:
    print(f"xvalue is {x},y value is {y}")
    x+=1
    y-=1
