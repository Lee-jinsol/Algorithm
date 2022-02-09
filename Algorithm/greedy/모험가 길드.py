#모험가 길드 문제 

num, scary = map(int,input().split('/')


1 2 2 2 3
 #오름차순 정렬 이후에 공포도가 가장 낮은 모험가부터 하나씩 확인

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹수 
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)