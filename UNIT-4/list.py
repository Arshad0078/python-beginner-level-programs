#list are declared within square brackets
list1 = [23,45,66,45,"python","h",12.45]
#access by index
print(list1[0])
#updateing the element since list is mutable
list1[0]=100
print(f"after updating the list\n{list1}")
list1.append(40)
print(f"aftter appending 40 at end \n {list1}")
list1.insert(2,50)
print(f"after inserting 50 at index 2\n{list1}")
del list1[3]
print(f"after deleting the element at index 3\n{list1}")
list1.remove("h")
print(f"after removing the element 'h'\n{list1}")
#del list1
#print(list1)
#nested list
listed = [0,23,[24,56,78]]
#tthe whole list inside the list is considered as one element
print(listed[2])
#to access each element in the nested list
print(listed[2][0])
#cloning
list2 = list1
list3 = list1[2:]

#list opreation
print(len(list2))
print(list1+list3)
print('python' in list1)
print('python' not in list2)
print(list1*3)
# print(max(list1))
# print(min(list1))
# print(sum(list2))
# print(all(list2))

#list aliasing
#it means both object pointing at the same memory location
list1 = [1,2,3,4,5]
list2 = list1
print(list2)
list2[0] = 10
print(list2)
print(list1)

#list methods

list2 = [x for x in range(0,11)]
#append
print("before append",list2)
list2.append(24)
print('after append',list2)
#count
print(list2.count(8))
#index
print(list2[5])
#insert
list2.insert(6,100)
print(list2)
#pop()
list2.pop()
print(list2)
#remove
list2.remove(100)
print(list2)
#reverse
list2.reverse()
print(list2)
#sort
list2.sort()
print(list2)
#extend
list2.extend([1,2,3])
print(list2)

#list looping

list1 = [1,2,3,4,5]
sum =0
for i in list1:
    sum+=i
print("sum of the list is",sum)
print(sum/float(len(list1)))

#enumerate
list2 = [x for x in range(0,11)]
for index,i in enumerate(list2):
    print(i," is at index : ",index)

#using range
for i in range(len(list2)):
    print("index :",i)

