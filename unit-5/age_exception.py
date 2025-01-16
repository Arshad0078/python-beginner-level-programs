try:
    n = int(input("enter age"))
except ValueError:
    print("enter valid age")
else:
    print("i see that you are %d years old"%n)
    print('Goodbye!')