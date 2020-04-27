mem1=[]
mem = []
X = ""
while X != "SCHOOL":
    X = input()
    mem.append(X)

mem.reverse()
mem1.append(mem[-1])
mem1.append("HOME")
del mem[-1]


for i,p in enumerate(mem):
    if p == "R":
        print(f"Turn LEFT onto {mem[i+1]} street.")
    elif p == "L":
        print(f"Turn RIGHT onto {mem[i + 1]} street.")

for i,p in enumerate(mem1):
    if p == "R":
        print(f"Turn LEFT into your HOME.")
    elif p == "L":
        print(f"Turn RIGHT into your HOME.")

