#시뮬레이션 유형
#L 왼쪽으로 한칸 
#R 오른쪽으로 한칸
#U 위로 한칸
#D 아래로 한칸

n = int(input())
plans = input().split()

x,y = 1,1

dx = [0,0,-1,1] #행
dy = [1,-1,0,0] #열
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny <1 or nx > n or ny > n:
        continue

    x,y = nx, ny

    print(x,y)





for i in 100 :
    for j in 100:
