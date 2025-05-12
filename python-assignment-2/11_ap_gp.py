wrongAP = [2, 5, 8, 11, 14, 15]
wrongGP = [3, 9, 27, 81, 9999, 729]

def setcorrectAP(wrongAP):
    AP = wrongAP
    differenceAp = [AP[i+1] - AP[i] for i in range(len(AP) - 1)]
    most_frequent_differnce = max(differenceAp, key=differenceAp.count)

    for i in range(len(AP) - 1):
        if AP[i+1] - AP[i] != most_frequent_differnce:
            AP[i+1] = AP[i] + most_frequent_differnce
        
    return AP

def setcorrectGP(wrongGP):
    GP = wrongGP
    divGP = [GP[i+1] / GP[i] for i in range(len(GP) - 1)]
    most_frequent_div = max(divGP, key=divGP.count)

    for i in range(len(GP)-1):
        if GP[i+1] // GP[i] != most_frequent_div:
            GP[i] = int( GP[0] * most_frequent_div**i)

    return GP

print("correct AP : ", setcorrectAP(wrongAP))
print("")
print("correct GP : ", setcorrectGP(wrongGP))