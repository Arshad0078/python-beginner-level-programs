f = open("sample.txt",'w')
print(f.mode)
print(f.name)
name = input("enter your name:").lower().lstrip().rstrip().title()
age = int(input("enter your age:"))
f.write(f"Name : {name}")
f.write("\n")
f.write(f"Age  :{str(age)}")
f.close()
print(f.closed)
