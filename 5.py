n = int(input())

road = []
result = []
for i in range(n): 
    road.append(input())
    result.append([0, 0, 0])
    
#start with end of road
for i in range(3): 
    if(road[-1][i] == "C"): result[-1][i] += 1

for i in range(n-2, -1, -1):
    for j in range(3):
        # next cell if there is W
        if road[i][j] == "W": continue
        # check alternatives
        for a in range(j-1, j+2):
            # if it is not forbidden to move and not W
            if(a >= 0 and a < 3 and road[i + 1][a] != 'W'):
                # count C
                cc = 1 if (road[i][j] == "C") else 0
                # find max C
                result[i][j] = max(result[i + 1][a] + cc,result[i][j])

print(max(result[0]))