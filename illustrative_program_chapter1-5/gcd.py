def gcd(n1,n2):
    rem = n1%n2
    if rem==0:
        return n2
    else:
        return gcd(n2,rem)

n1=int(input("enter n1:"))
n2 = int(input("enter n2:"))
print("gcd of",n1,"and",n2,"is",gcd(n1,n2))