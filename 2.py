nm = list(map(int, input().split(' ')))
n = nm[0]
m = nm[1]

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split(' '))))

result = []   
for mm in range(m):
    temp = []
    for nn in range(n-1, -1, -1):
        temp.append(matrix[nn][mm])
    result.append(temp)

for i in result:
    print(*i, sep=' ')
