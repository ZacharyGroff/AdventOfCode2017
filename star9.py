with open('day5input') as f:
   myList = [line.rstrip('\n') for line in f]

myList = list(map(int, myList))
steps = 0
i = 0

while(True):
    try:
        temp = i
        i += myList[i]
        steps += 1
        myList[temp] += 1
    
    except IndexError:
        break

print(steps)
