#시작점 0 끝점 19 중간점 9 
n, m = map(int, input().split())
array = list(map(int, input().split()))

first = 0
last = max(array)

result = 0

while (first <= last):
    a_sum = 0
    mid = (first+last) // 2
    for i in array :
        if i > mid:
            a_sum += i - mid
    if a_sum < m:
        last = mid -1    
    else:
        result = mid
        first = mid +1 

print(result)



