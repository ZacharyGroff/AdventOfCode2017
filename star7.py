from collections import Counter
badList = (open('passcodes', 'r').read().splitlines())
result = 0

for i in badList:
    temp = i.split()
    count = 0
    for x in temp:
        if (temp.count(x) != 1):
            break
        else:
            count += 1
        if (count == len(temp)):
            result += 1
    

print(result)
