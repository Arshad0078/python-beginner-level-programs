def linear_search(a,target):
    for i in range(len(a)):
        if a[i]==target:
            print("element is found at position %d"%(i+1))
            return
    print("element is not found in the list")
list = [23,56,446,34,74,76,46,89,12,38]
target = 69
linear_search(list,target)