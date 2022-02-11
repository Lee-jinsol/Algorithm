탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정 
=> 대표적인 그래프 탐색 알고리즘으로는 DFS & BFS 가 있음

<hr/>

스택 자료구조 
- 먼저 들어온 데이터가 나중에 나가는 형식
- 선입후출 
- 입구와 출구가 동일한 형태 
- 예) 박스 쌓기 

스택 동작 
- 삽입 또는 삭제
- 리스트 자료형 사용 

```
stack = []

stack.append(5)
stack.pop()

print(stack[::1]) #최상단 원소부터 출력 (먼저 나가고자 하는 원소)
print(stack) #최하단 원소부터 출력

```

큐 자료구조 
- 먼저 들어온 데이터가 먼저 나가는 형식
- 선입선출
- 입구와 출구가 모두 뚫려 있는 터널과 같은 형태 
- 일종의 대기열
- 리스트 자료형도 사용 가능하지만 시간 복잡도가 높아서 효율이 낮기 때문에 deque 라이브러리 사용
- 구현시 => 오른쪽으로 들어와서 왼쪽으로 나간다 

```
queue = deque()

queue.append(5)
queue.popleft()

print(queue) #먼저 들어온 순서대로 출력

```

<hr/>


### DFS (Depth-First Search )
- 깊이 우선 탐색 
- 깊게 들어가다가 더 이상 들어갈 곳이 없다면 끝 
- 그래프의 깊은 부분을 우선적으로 탐색하는 알고리즘
- 스택 & 재귀함수를 이용

1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 방문하지 않은 노드가 하나라도 있으면 스택에 넣고 방문 처리를 한다.
3. 2번의 과정을 수행할수 없을때 까지 반복한다.

![](https://images.velog.io/images/jinsol/post/185324e4-6455-4cb5-9fe5-d313acbb73b8/image.png)

```
# DFS 함수 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
```

<hr/>

### BFS ( Breadth-First Search)
- 너비 우선 탐색
- 가까운 노드부터 우선적으로 탐색
- 큐 자료구조 이용
- 최단거리 문제에서 자주 사용

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 함
2. 큐에서 노드를 꺼낸뒤에 인접 노드중 방문하지 않은 노드를 모두 큐에 삽입하고 방문함
3. 2번 과정 수행할 수 없을 때가지 반복

![](https://images.velog.io/images/jinsol/post/b4665b1f-4b54-4828-8d2a-32dbc33e237e/bfs.png)

탐색 순서 : 1 > 2 > 3 > 8 > 7 > 4 > 5 > 6

```
from collections import deque

# BFS 함수 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
#visted 라는 이름의 리스트 생성
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)```

```

<hr/>
