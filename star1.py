myList = input()
myList = [int(d) for d in str(myList)]
result = 0
for i in range (len(myList) - 1):
    if (myList[i] == myList[i+1]):
        result += myList[i]
if (myList[0] == myList[-1]):
    result += myList[-1]
print(result)
