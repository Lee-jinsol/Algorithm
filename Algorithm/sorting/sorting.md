#### 정렬이란
데이터를 특정 기준에 따라 순서대로 나열하는 것 

1. 선택 정렬 
- 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복
- 시간 복잡도 : O(N제곱)

```
array = [5,2,6,1]
for i in range (len(array)):
	min_index = i
    for j in range(i+1, len(array)):
    	if array[min_index] > array[j]:
        	min_index = j
    array[i], array[min_index] = array[min_index], array[i] #스와프
    
print(array)
    	
```

2. 삽입 정렬
- 처리 되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
- 일반적으로 선택 정렬보다 더 효율적으로 동작함  
- 시간 복잡도 : O(N제곱)
```
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)
```

3. 퀵 정렬
- 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법 
- 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 
- 첫 번째 데이터를 기준 데이터(Pivot)로 설정함
- 시간 복잡도 : O(NlogN)
- 하지만 최악의 경우(이미 정렬된 배열에 대해서 퀵 정렬을 할 경우) : O(N제곱)이 될 수도 있다. 

```
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```

4. 계수 정렬
- 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때
- 매우 빠르게 동작함 
- 시간 복잡도 : O(N+K)

```
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
```
![](https://images.velog.io/images/jinsol/post/e100b995-156f-417e-8ec0-79631d771db7/image.png)
