Lines = int(input())
Z = input().split()
Z = [int(i) for i in Z]
print(f"{max(Z) - min(Z)}")