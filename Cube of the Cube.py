def cube(x):
    return x**3

def by_three(x):
    if x %3==0:
        return cube (x)
    else:
        return False
    
print(by_three(9))
print(by_three(4))
