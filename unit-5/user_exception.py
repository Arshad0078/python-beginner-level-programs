class Error(Exception):
    pass
class PosError(Error):
    pass
class NegError(Error):
    pass
try:
    num = int(input("enter num:"))
    if num<0:
        raise NegError
        break
    else:
        raise PosError
except PosError:
    print("this value is positive")
except NegError:
    print("this value is negative")