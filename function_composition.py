import functools

def compose(*functions):
    def composed_function(x):
        for f in reversed(functions):
            x = f(x)
        return x
    return composed_function

def square(x):
    return x**2

def inc(x):
    return(x+1)

inc_and_square = compose(square, inc)
res = inc_and_square(9)
print(res)  # Output: 100
