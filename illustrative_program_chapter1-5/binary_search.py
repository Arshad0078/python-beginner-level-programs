def binary_search(a,val):
    first = 0
    last = len(a)-1
    found = False
    while first<=last and not found:
        mid = (first+last)//2
        if a[mid]==val:
            print("value found at position",mid+1)
            found = True
            break
        elif a[mid]<val:
            first = mid+1
        else:
            last = mid-1
    if found!=True:
        print("element not present in the list")
list = [12,16,34,42,56,78,88,98]
target = 34
binary_search(list,target)