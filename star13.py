from collections import Counter
c = Counter()
elements = []

with open('day7input') as f:
    lines = f.readlines()
for line in lines:        
    line = line.replace(',', '')     
    temp  = (list(line.split()))
    elements.append(temp)
       
for element in elements:
    del element[1]
    for x in set(element):
        c[x] += 1

for element in c:
        if c[element] == 1:
            print(element)
