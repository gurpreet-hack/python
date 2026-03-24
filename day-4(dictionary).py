#---> Create dictionary
a={"name":"Aryan","roll no":"512","name":"Aryan"}
print(a)
b={"dict":a}
print(b)

#---> methods to print key
print(a.get("name"))
print(a["name"])

#---> Add key to dictionary
a["age"]="21"
print(a)
print(a.keys())

#---> Update key name
a["name"]="Arshita"
print(a)
a.update({"name":"gurpreet"})
print(a)

#---> Remove key 
a.pop("name")
print(a)
a.popitem()            #it will remove recent inserted key:value
# print(a)
# del a
print(a)
a.clear()
print(a)

#---> Loop
a={"name":"arshita","age":"20"}
for i in a:
    print(i,a[i])

for i in a.values():
    print(i)

for i in a.keys():
    print(i)

for x,y in a.items():
    print(x,y)

#---> Copy
b=a.copy()
print(b)

#---> Nested Dictionary
myfamily = {
  "child1" : {
    "name" : "Alicia",
    "year" : 2004
  },
  "child2" : {
    "name" : "Ares",
    "year" : 2007
  },
  "child3" : {
    "name" : "Erica",
    "year" : 2011
  },
  "child4" : {
    "name" : "Jeremie",
    "year" : 2015
  }
}
for x,obj in myfamily.items():
    print(x)
    for y in obj:
        print(y,":",obj[y])

#---> fromkeys()
x={"key1","key2","key3"}
y=0
z=dict.fromkeys(x,y)
print(z)
#OR
a={"std1","std2","std3"}
b=10
c=dict.fromkeys(a,b)
print(c)

#---> setdefault()
x={
    "model":"Mustang",
    "brand":"ford",
    "year":1964
}
y=x.setdefault("model","Bronco")
print(y)
#OR
a={"brand":"ford",
   "year":1964
   }
b=a.setdefault("model","Bronco")
print(b)