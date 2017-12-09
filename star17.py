myInput = open('day9input').read()
count = 0
countScore = 0
score = 0
ignore = False
stack = []


while True:
    
    if count >= len(myInput):
        break
    
    if myInput[count] == '!':
        count += 1
    
    elif ignore:
        if myInput[count] == '>':
            ignore = False
    
    elif myInput[count] == '{':
        countScore += 1
        stack.append(countScore)
    
    elif myInput[count] == '<':
        ignore = True
    
    elif myInput[count] == '}':
        countScore -= 1
        score += stack.pop()
    
    count += 1
    
print(count)
