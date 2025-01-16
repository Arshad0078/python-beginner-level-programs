#required arguments take atlest 1 arguemnet
# def func(str):
#     print(str)
# #the correct way to do it
# str = "hello world"
# func(str)
#func()
#print(func("good"))#error becasue no argument is passed in the main function


#keyword arguments

# def display (str,int_x,float_y):
#     print("the string is :",str)
#     print("the integer is :",int_x)
#     print("the float is :",float_y)
# display(float_y=1456.34,str="hello world",int_x=2456)

#default arguments
# def show(name="not defined",course="B.tech"):
#     print("name "+name)
#     print("course "+course)
# show(course="B.ca",name="arun")
# show(name="Praveen")
# show()

#variable length arguments if dont know how many arguments will be passed we use asterick(*)
def fav(name,*fav_sub):
    print("\n",name,"likes to read")
    for fav in fav_sub:
        print(fav,end=" ")
fav("arshad","python","c++","gaming")
fav("lopal","hacking","programming","maths")
fav("ars")