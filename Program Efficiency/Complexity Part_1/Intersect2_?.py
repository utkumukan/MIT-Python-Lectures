def intersect(L1, L2):
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    return tmp

testList1 = [1, 3, 4, 5, 7, 9, 18, 27]

testList2 = [1, 9, 16, 65, 70]

print("result: ", intersect(testList1, testList2))