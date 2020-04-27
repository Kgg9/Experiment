mem = []
for i in range(10):
    A,B,C,D = input().split()
    stu = int(input())
    Y = 0
    for i in range(stu):
        a, b, c, d = input().split()
        X = (float(a) * float(A)/100) + (float(b) * float(B)/100) + (float(c) * float(C)/100) + (float(d) * float(D)/100)
        if X > 49.9:
            Y+=1
    mem.append(Y)

mem = [print(i) for i in mem]





