with open('day5input') as f:
   myList = [line.rstrip('\n') for line in f]

myList = list(map(int, myList))
steps = 0
i = 0

while(True):
    try:
        temp = i
        if (myList[i] < 3):
            i += myList[i]
            myList[temp] += 1
        else:
            i += myList[i]
            myList[temp] -= 1
        steps += 1
    
    except IndexError:
        break

print(steps)

