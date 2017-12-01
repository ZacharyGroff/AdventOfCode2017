def splitList(myList):
    half = len(myList)//2
    return myList[:half], myList[half:]

myList = input()
myList = [int(d) for d in str(myList)]
steps = len(myList) // 2
result = 0
myList1, myList2 = splitList(myList)

for i in range (len(myList1) - 1):
    if (myList1[i] == myList2[i]):
        result += (myList1[i] * 2)
print(result)


