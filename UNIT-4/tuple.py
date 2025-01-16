#tuple assignment
# (val1,val2,val3)=(1,2,3)
# print(val1,val2,val3)
# Tup1 = (100,200,300)
# val,val2,val3 = Tup1
# print(val,val2,val3)
# val1,val2,val3 = (2+4,5/3+4,9%6)
# print(eval1,val2,val3)


#tuple returning mutiple values
def max_min(values):
    x = max(values)
    y = min(values)
    return x,y
values = (99,98,90,97,89,86,93,82)
(max_value,min_value) = max_min(values)
print("max value is:",max_value)
print("min value is:",min_value) 
