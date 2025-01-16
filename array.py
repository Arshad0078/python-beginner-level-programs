import array
ar_ray = array.array('i',[1,34,56,78,90])
#traverse
for x in ar_ray:
    print(x,end=" ")
#access
print("\nAccessing elements using index",ar_ray[3])
#insert
ar_ray.insert(3,100)
print("After inserting 100 at index 3")
for x in ar_ray:
    print(x,end=" ")
#delete
ar_ray.remove(100)
for x in ar_ray:
    print(x,end=" ")
#search element in array
print('\n 1 is present in the array at index :')
print(ar_ray.index(1))
#update
ar_ray[4]=34
print("\n after update:")
for x in ar_ray:
    print(x,end=" ")
      