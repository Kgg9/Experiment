Lines = int(input())
z = [int(input()) for i in range(Lines)]
PO = z[0]
del z[0]
z = [i for i in z if i >= PO]
if len(z) == 0:
    print("YES")
else:
    print("NO")


