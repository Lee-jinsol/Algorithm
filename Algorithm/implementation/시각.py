#시각 문제
#완전 탐색
 
 n = int(input())

count = 0

for i range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)