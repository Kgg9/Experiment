a, b = input().split()
Z = [int(i) for i in input().split()]
Z.sort()
print(sum(Z[-int(b):]))
