# num1 = 10 #global scope variable
# print("global scope :",num1)
# def func(num2):
# a=10 #global variable
# b=20 #global variable
# defined_c = False
# def add(a,b):
#     c =a+b #local variable
#     return c
# print(add(a,b)) #passing parameter to the function
# print(f"global variables{a}{b}") #printing global variables
# print(f"local variables{c}") # hopefully i have to get a error


#use global scope variable inside a function
# var = "good"
# def show():
#     global var1 # variable is declared as global
#     var1 = "morning"
#     print("in function var is - ",var)
# show()
# print("outside function var1 is - ",var1) # it will work now because the variable is declared as globale
# print("var is -",var)


# same variable can be used as local and global variable at the same time
# var = "good"
# def show():
#     var = "morning"
#     print("in function var is - ",var)
# show()
# print("outside function var is - ",var)

# if we declare global variable in bot inside channges are reflected
# var ="good"
# def show():
#     global var
#     var = "morning"
#     print("in function var is - ",var)
# show()
# print("outside function var is - ",var)
# var = 'fantastic'
# print("outside function after modification,var is - ",var)


