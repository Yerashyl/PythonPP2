from math import sqrt
n = int(input())
def is_sqrt(x):
    y = sqrt(x)
    x = y%1
    if x==0:
        return True
    return False
def gen_num():
    num = 1
    while num<=n:
        if is_sqrt(num):
            yield num
        num += 1
for i in gen_num():
    print(i)