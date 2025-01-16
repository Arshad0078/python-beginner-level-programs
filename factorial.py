# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# n=int(input("enter n:"))
# print("factorial of",n,"is",fact(n))mi

#without using recursion
num =int(input("enter a:"))
i = num
result =1
while i>=1:
    result = result * i
    i = i-1
print("factorial of",num,"is : ",result)