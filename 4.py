
n, direction = input().split()
n = int(n)

swaps = []
matrix = []

for i in range(n): matrix.append(list(map(int, input().split(' '))))

if(direction == 'R'):
    for i in range(n//2):
        for j in range(i,n-1-i):
            # shift the numbers in a "circle"
                swaps.append(f"{i} {j} {j} {n-1-i}")
                swaps.append(f"{i} {j} {n-1-i} {n-1-j}")
                swaps.append(f"{i} {j} {n-1-j} {i}")
                
elif(direction == 'L'):
    for j in range(n//2):
        for i in range(j,n-1-j):
            # shift the numbers in a "circle"
                swaps.append(f"{i} {j} {n-1-j} {i}")
                swaps.append(f"{i} {j} {n-1-i} {n-1-j}")
                swaps.append(f"{i} {j} {j} {n-1-i}")

print(len(swaps))
for i in swaps: print(*i)