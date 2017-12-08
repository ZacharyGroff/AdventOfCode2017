myList = []
registerValues = dict()

with open('day8input') as lines:
    for line in lines:
        myList.append(line.split())

#set all registers to 0
for i in myList:
    registerValues[i[0]] = 0

for i in myList:
   
    if i[5] == '!=':
        if registerValues[i[4]] != int(i[6]):
            if i[1] == 'inc':
                registerValues[i[0]] += int(i[2])
            elif i[1] == 'dec':
                registerValues[i[0]] -= int(i[2]) 
    
    elif i[5] == '>':
        if registerValues[i[4]] > int(i[6]):
            if i[1] == 'inc':
                registerValues[i[0]] += int(i[2])
            elif i[1] == 'dec':
                registerValues[i[0]] -= int(i[2]) 
   
   elif i[5] == '>=':
        if registerValues[i[4]] >= int(i[6]):
            if i[1] == 'inc':
                registerValues[i[0]] += int(i[2])
            elif i[1] == 'dec':
                registerValues[i[0]] -= int(i[2]) 
    
    elif i[5] == '<':        
        if registerValues[i[4]] < int(i[6]):
            if i[1] == 'inc':
                registerValues[i[0]] += int(i[2])
            elif i[1] == 'dec':
                registerValues[i[0]] -= int(i[2]) 
    
    elif i[5] == '<=':
        if registerValues[i[4]] <= int(i[6]):
            if i[1] == 'inc':
                registerValues[i[0]] += int(i[2])
            elif i[1] == 'dec':
                registerValues[i[0]] -= int(i[2]) 
    
    elif i[5] == '==':
        if registerValues[i[4]] == int(i[6]):
            if i[1] == 'inc':
                registerValues[i[0]] += int(i[2])
            elif i[1] == 'dec':
                registerValues[i[0]] -= int(i[2]) 
    else:
        print('error', i[5])
    
print(registerValues)
