def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                return matched
            if e1 != e2:
                return False
    return

testList1 = [1, 3, 4, 5, 7, 9, 18, 27]

testList2 = [16, 65, 70]

print("result: ", isSubset(testList1, testList2))