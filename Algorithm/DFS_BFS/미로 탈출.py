from collections import deque

n,m = map(int, input().split())

graph =[]
for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))
def bfs(x,y):
    #큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    #큐가 빌 때까지 반복하기 
    while queue:
        x,y = queue.popleft()
        #현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[y]
            #공간 벗어난 경우 무시 
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            #괴물이 있는 경우 무시
            if graph[nx][ny] == 0:
                continue
            #해당 노드를 처음 방문 하는 경우 , 최단 거리 기록
            if graph[nx][ny] == 1:
                 graph[nx][ny] = graph[x][y] + 1
                 queue.append((nx,ny))
    return graph[n-1][m-1]
 



