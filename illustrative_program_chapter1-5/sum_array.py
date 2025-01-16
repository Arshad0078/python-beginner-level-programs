import array
ARR = array.array('i',[23,45,67,89,0,2,34,56,24])
sum = 0 
for a in ARR:
    sum+=a
print(f"sum of the array is {sum}")
