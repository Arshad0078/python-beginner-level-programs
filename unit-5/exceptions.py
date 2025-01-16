# #zero division error
# try:
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("any value cannot be divided by zero")
#     x =[y for y in range(1,150)]
#     while b not in x:
#         b = int(input("enter a number greater than zero"))
#     c=a/b
#     print(c)
# except ValueError:
#     print("please enter a number")

 #raise exception
try:
    raise ValueError
except ValueError:
    print("error")       