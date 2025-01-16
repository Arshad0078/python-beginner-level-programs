#write
import random
f = open("test1.txt",'w+')
options = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", 
    "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", 
    "strawberry", "tangerine", "ugli fruit", "vanilla", "watermelon", "apricot", 
    "blackberry", "cantaloupe", "dragonfruit", "eggplant", "fennel", "garlic", 
    "horseradish", "jalapeño", "kale", "lettuce", "mushroom", "nutmeg", "onion", 
    "parsley", "quinoa", "radish", "spinach", "tomato", "zucchini", "artichoke", 
    "broccoli", "carrot", "daikon", "endive", "fiddlehead", "green bean", 
    "hubbard squash", "iceberg lettuce", "jicama", "kohlrabi", "leek", "mangetout", 
    "napa cabbage", "okra", "parsnip", "pumpkin", "rhubarb", "sorrel", "turnip", 
    "watercress", "yam", "zucchini", "almond", "brazil nut", "cashew", "chestnut", 
    "hazelnut", "macadamia", "pecan", "pine nut", "walnut", "coconut", "peanut", 
    "pumpkin seed", "sunflower seed", "chia seed", "flaxseed", "sesame seed", 
    "hemp seed", "quinoa", "amaranth", "barley", "buckwheat", "corn", "millet", 
    "oats", "rice", "sorghum", "spelt", "wheat", "teff", "rye", "couscous", 
    "bulgur", "farro", "freekeh", "kasha", "polenta", "tapioca", "arrowroot"]
f.write("python is a programming language")
for i in range(0,11):
    choice = random.choices(options)
    f.write(f"\n {choice}")
f.close()
#read
f = open("test1.txt",'r+')
e=f.readline()
r=f.readlines()
print(e)
print(r)
f.close()

#file position
#tell
file =open("test2.txt","w+")
str1 ="python is a programming language"
file.write(str1)
file.close()
file = open("test2.txt","r+")
k = file.read(20)
print(f"the string read is {k}")
pos = file.tell();
print(f"current position is {pos}")
pos = file.seek(0,0)
str3 = file.read(10)
print(f"string read after seek is {str3}")
file.close()


#format operator
#format string
name = input('enter your name')
print("hello %s welcome to python programming"%name)
#format integer
age = None
list = [x for x in range(0,100)]
while age not in list:
    age = int(input("enter your age:"))
print("hello %s you are %d years old "%(name,age))
#float
point = float(input("enter a floating point"))
print("your point is %f "%(point))
