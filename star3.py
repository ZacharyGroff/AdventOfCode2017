result = 0
with open('spreadsheet', 'r') as f:
    spread = [row.strip().split() for row in f.read().splitlines()]
for row in spread:
    integers = list(map(int,row))
    result += (max(integers) - min(integers))    
print(result)
