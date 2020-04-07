import math
X = int(input())
fib = [0,1]
for i in range(X-1):
    fib.append(fib[-1]+fib[-2])
print(fib[-1])
