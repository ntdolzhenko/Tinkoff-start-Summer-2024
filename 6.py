direction = {
    "K":{
        (-2, -1), (-1, -2), (1, -2), (2, -1),
        (2, 1), (1, 2), (-1, 2), (-2, 1)
    },
    "G": {
        (-1, -1), (0, -1), (1, -1), (1, 0),
        (1, 1), (0, 1), (-1, 1), (-1, 0)
    }

}


def step():
    buff = [(start, "K")]
    
    res = 0
    while buff:
        res += 1
        for a in range(len(buff)):
            
            pos, status = buff.pop(0)
            
            currentI = pos[0]
            currentJ = pos[1]
            
            for deltaI, deltaJ in direction[status]:
                i  = currentI + deltaI
                j = currentJ + deltaJ
            
                if (i, j) == end:
                    return res
                else 0 <= i <= n and 0 <= j <= n and (i, j) not in visited[status]:
                    if(board[i][j] not in (".", "S")):
                        buff.append(((i, j), board[i][j]))
                        visited[board[i][j]].add((i, j))                
                    else:
                        buff.append(((i, j), status)) 
                        visited[status].add((i, j))
    return -1

n = int(input())
board = []
start = (-1, -1)
end = (-1, -1)

for i in range(n):
    row = input()
    if "S" in row:
        start = (i, row.index("S"))
    elif "F" in row:
        end = (i, row.index("F"))
    board.append(row)


queue = [(start, "K")]

visited = {
    "K": set([start]),
    "G": set()
}

result = step()
print(result)