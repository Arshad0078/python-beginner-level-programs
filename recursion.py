#gcd
def GCD(x,y):
    rem = x%y
    if rem == 0:
        return y
    else:
        return GCD(y,rem)
n = int(input("enter the first number:"))
m = int(input("enter the second number:"))
print("GCD of",n,"and",m,"is",GCD(n,m))