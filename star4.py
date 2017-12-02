result = 0
with open('spreadsheet', 'r') as f:
    spread = [row.strip().split() for row in f.read().splitlines()]
for row in spread:
    values = list(map(int,row))
    for x in values:
        for y in values:
            if x % y == 0 and x != y:
                print(x,y)
                result += (x/y)
print(result)
