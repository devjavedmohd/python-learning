import random

i = 100
j = 20e7
a = random.randrange(i, j)

try:
    b = random.randrange(j, i)
except ValueError:
    print('ValueError on randrange() since start > stop')



