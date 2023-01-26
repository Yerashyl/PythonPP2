a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a1%2==0 and b1%2==0:
    if (a2%2==0 and b2%2==0) or (a2%2!=0 and b2%2!=0):
        print("YES")
    else: print("NO")
elif a1%2==0 and b1%2!=0:
    if (a2%2!=0 and b2%2==0) or (a2%2==0 and b2%2!=0):
        print("YES")
    else: print("NO")
elif a1%2!=0 and b1%2==0:
    if (a2%2!=0 and b2%2==0) or (a2%2==0 and b2%2!=0):
        print("YES")
    else: print("NO")
elif a1%2!=0 and b1%2!=0:
    if (a2%2==0 and b2%2==0) or (a2%2!=0 and b2%2!=0):
        print("YES")
    else: print("NO")
