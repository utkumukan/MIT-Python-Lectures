def bisect_search(L, e):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)//2
        if L[half] > e:
            return bisect_search(L[:half], e)
        else:
            return bisect_search(L[half:], e)

testList = []
for i in range(100):
    testList.append(i)

print(bisect_search(testList, 156))