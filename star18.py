with open('day9input') as f:
    myInput = f.read()

count = 0
countScore = 0
score = 0
ignore = False
stack = []
trash = 0


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
    
    if ignore and myInput[count] != '>' and myInput[count] != '!':
        trash += 1

print(trash)
