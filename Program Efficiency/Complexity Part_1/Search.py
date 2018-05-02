def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return

testList = [1, 3, 4, 5, 7, 9, 18, 27]

print("result:", search(testList, 26))