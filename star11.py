myList = list(map(int, input().split()))
seen = []

while(True):
    temp = myList[myList.index(max(myList))]
    tempPos = myList.index(max(myList))
    myList[myList.index(max(myList))] = 0
    
    for _ in range(temp):
        tempPos += 1
        myList[tempPos % len(myList)] += 1
        
    if myList in seen:
        break

    seen.append(myList[:])
print(len(seen)+1)
