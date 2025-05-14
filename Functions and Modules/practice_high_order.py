import functools
lst = [0,-2,1,4]
print(functools.reduce(lambda x,y:x+y,lst))