def Checker(Y):
    YY = str(Y)
    if YY.count("1") >=2:
        return False
    if YY.count("2") >=2:
        return False
    if YY.count("3") >=2:
        return False
    if YY.count("4") >=2:
        return False
    if YY.count("5") >=2:
        return False
    if YY.count("6") >=2:
        return False
    if YY.count("7") >=2:
        return False
    if YY.count("8") >=2:
        return False
    if YY.count("9") >=2:
        return False
    if YY.count("0") >=2:
        return False

X = int(input()) + 1
while Checker(X)==False:
    X+=1
print(X)







