def swapping_temp(a,b):
    print(f"before sorting : {a},{b}")
    temp = a
    a =b
    b=temp
    print(f"after sorting : {a},{b}")
    return a,b
def swapping_directly(a,b):
    print(f"before sorting : {a},{b}")
    a,b=b,a
    print(f"after sorting : {a},{b}")
    return a,b
a=int(input("enter a number:"))
b = int(input("enter b number:"))
choice = int(input("which method do you want to swap (with temp(1),without temp(2)):"))
if choice==1:
    print(swapping_temp(a,b))
else:
    print(swapping_directly(a,b))