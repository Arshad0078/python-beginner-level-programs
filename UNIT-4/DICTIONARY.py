dict2 = {"name" :"xxx",
         "age"  :23,
         "class":5}
#accessing the element or we can say key
print(dict2["name"])
#adding or modifying an item
print(dict2['name'])
print(dict2["age"])
print(dict2["class"])
dict2['mark'] = 67
print(dict2['mark'])
#modifying an entry
dict2 = {'roll-no':81232,
         'name':'arav',
         'course':'B.Tech'}
print("Dict[Roll_NO] = ",dict2['roll-no'])
print("Dict[Name] = ",dict2['name'])
print("Dict[course] = ",dict2['course'])
dict2['course']='Bca'
print("Dict[course] = ",dict2['course'])
del dict2['roll-no']
#print("Dict[roll-no] = ",dict2['roll-no']) error because roll-no is deleted
#deleting all entries
dict2.clear()
#print("Dict[roll-no] = ",dict2['roll-no']) error because dict2 is cleared
#deleting the dictionary
#del dict2
#print("Dict[roll-no] = ",dict2['roll-no']) error because dict2 is deleted entirely
dict2.pop('name')
dict2.pop('age')