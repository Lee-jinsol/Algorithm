from itertools import combinations

n, run_chick = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1 : 
            house.append((i,j))
        else if [i][j] == 2 : 
            chicken.append((i,j))

for ch in combinations(chicken, run_chick):
    sum = 0
    for home in house:
        sum += min([abs(home[0]-i[0])+abs(home[1]-i[1]) for i in ch])
        if 