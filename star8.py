from collections import Counter
badList = (open('passcodes', 'r').read().splitlines())
result = 0

for i in badList:
    temp = i.split()
    temper = []
    count = 0
    for x in temp:
        temper.append(sorted(x))
    for x in temper:
        if (temper.count(x) != 1):
            break
        count += 1
        if (count == len(temper)):
            result += 1

print(result)
