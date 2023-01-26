x = int(input())
y = int(input())
z = int(input())
if x==y:
    if y==z:
        print(3)
    elif y!=z:
        print(2)
elif x!=y:
    if x==z and y!=z:
        print(2)
    elif x!=z and y==z:
        print(2)
    else: print(0)
