#chained if
a = input("enter your mark")
b = int(a)
if b>90:
    print("grade A")
elif b>80 and b<=90:
    print("grade B")
elif b>70 and b<=80:
    print("grade C")
elif b>45 and b<=70:
    print("grade D")
else:
    print("fail")
#nested if an if inside another if
a = int(input("enter a:"))
b = [3,5,7]
if a%2!=0:
    if a in b:
        print("it is a prime number")
    else:
        print("it is not a prime number")
else:
    print("it is not a odd number")
#while loop
n = int(input("enter a number"))
i =1 
while i<=n:
    print(i,end=" ")
    i+=1
#for loop 
n = int(input("enter a number:"))
for i  in range(1,n+1):
    print(i)
#inline condtion
a=40
b=20
print("a is greater than b") if a>b else print("a is smaller than b")
#sequence in loop 
a = [10,20,'hi','hello','python',12.23]
for i in a:
    print(i)
print(list(range(1,10,2)))