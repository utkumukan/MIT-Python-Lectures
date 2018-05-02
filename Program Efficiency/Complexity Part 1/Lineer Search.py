def Lineer_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found

testList = [1, 3, 4, 5, 7, 9, 18, 27]

print(Lineer_search(testList, 5))