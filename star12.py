myList = list(map(int, input().split()))
seen = []
final = 0
while(True):
    temp = myList[myList.index(max(myList))]
    tempPos = myList.index(max(myList))
    myList[myList.index(max(myList))] = 0
    
    for _ in range(temp):
        tempPos += 1
        myList[tempPos % len(myList)] += 1
        
    if myList in seen:
        final = seen.index(myList)
        break

    seen.append(myList[:])
print(len(seen) - final)
