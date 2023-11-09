c = 2
d = 8

def mystery(x):
    global c
    c = 5
    d = 12
    return c + d - x

print(mystery(10)+c+d)
