X = input()
LC = 0
UC = 0

for i in X:
    LC+=i.islower()
    UC+=i.isupper()

if LC > UC:
    print(X.lower())
elif UC > LC:
    print(X.upper())
elif LC == UC:
    print(X)