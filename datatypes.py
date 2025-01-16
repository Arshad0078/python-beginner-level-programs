#numbers
#int
a = 10 #whole numbers without decimal point
#float
b = 10.5 # with decimal floating point
#complex
c = 10+5j # with imaginary part
i = type(a)
p = type(b)
o = type(c)
print(f"{i}\n{p}\n{o}")
#boolean
z =True
x = False
print(f"boolean value1:{z}\n boolean value2:{x}")
#sequence
#string
h = "hello world"
#index
print(h[0]) #access 1st element in the list starting as 0
#mutability
#h[2]= "a" #this will give us error becuase strings are immutable
#concatentation
print(h+" world") #string concatenation
#repeating
print(h*3) #repeating string
#slicing
print(h[2:5]) # slices string from 2 to 4 index
#string stride slicing it takes 3 arguments [start:stop:step]
print(h[2:6:2]) # slices from 2 to 5 with 2 steps each skip 2 elemnts in betwweeen
#in not in
print('h' in h) # return true if h found in the string 
print('h' not in h) # return true if h not found in the string
#list
l = [1,2,3,4,5]
#index
print(l[0]) #access 1st element in the list starting as 0
#mutability
l[2]= 10 #this will give us no error becuase lists are mutable
#concatentation
print(l+[1,2,3]) #string concatenation
#repeating
print(l*3) #repeating string
#slicing
print(l[2:5]) # slices string from 2 to 4 index
#string stride slicing it takes 3 arguments [start:stop:step]
print(l[2:6:2]) # slices from 2 to 5 with 2
#in not in
print(1 in l) # return true if 1 found in the list
print(1 not in l) # return true if 1 not found in the list
#inserting element in the list
l.insert(2,"python")
print(l)
#removing element in the list
l.remove("python")
print(l)
#tuple
t = (1,2,3,4,5)
#index
print(t[0]) #access 1st element in the list starting as 0
#mutability
#t[2]= 10 #this will give us error becuase tuples are immutable
#slicing
print(t[2:5]) # slices string from 2 to 4 index
#string stride slicing it takes 3 arguments [start:stop:step]
print(t[2:6:2]) # slices from 2 to 5 with 2
#in not in
print(1 in t) # return true if 1 found in the tuple
print(1 not in t) # return true if 1 not found in the tuple
#set
set1 = {12,"python",25,"programming",10.5}
#unorderd
print(set1) #it will not appear as the same order
#unindexed
#print(set1[0]) #this will give us error becuase set is unindexed
#class
print(type(set1))
# in not in
print(25 in set1)
print(25 not in set1)
#update
a2 = [10,20,30,'a']
set1.update(a2)
print(set1)
#remove
set1.remove(25)
print(set1)
#add
set1.add(25)
print(set1)
#intersection
set1.intersection({12,25,10.5})
print(set1)
#symmetric
set1.symmetric_difference({12,25,10.5})
#dictionary 
dict = {"name":"arshad",
        "age":18,
        "city":"karachi"}
print(dict["name"])
#key value pair
print(dict.keys())
#len
print(len(dict))
print(dict['age'])
print(dict.get('age'))
#pop
print(dict.pop('age'))
print(dict)
#clear
dict.clear()
print(dict)

