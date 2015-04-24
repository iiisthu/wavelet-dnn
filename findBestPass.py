file_name = 'tester.log'
fin = open(file_name, 'r')
lines = fin.readlines()

Pass = 0
Cost = 999

for line in lines:
    vals = line.split()
    if len(vals) < 8 or line[0] != 'I':
        continue
    if vals[6][0] != 'A':
        continue

    currentCost = float(vals[6].split('=')[1])
    if currentCost < Cost:
        Cost = currentCost
        Pass = vals[4].split('=')[1]
        print Cost, Pass
        
print Pass, Cost

fin.close()
