import math
for Pussy in range(5):
    X = int(input())
    Z = [i for i in range(2,X+1)]

    i = 2
    while(i <= int(math.sqrt(X))):
        if i in Z:
            for j in range(i*2, X+1, i):
                if j in Z:
                    Z.remove(j)
        i = i+1

    Dick = []
    for i in range(len(Z)):
        numm = Z[i]
        for L in Z:
            Dick.append(L*numm)
        i+=1

    if X in Dick:
        print("semiprime")
    else:
        print("not")

