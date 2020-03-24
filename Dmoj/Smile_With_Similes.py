L1 = int(input())
L2 = int(input())
Z = [input() for i in range(L1)]
Y = [input() for i in range(L2)]
for i in Z:
    for L in Y:
        print(f"{i} as {L}")
