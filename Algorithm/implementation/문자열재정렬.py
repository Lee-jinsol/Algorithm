# 문자열 재정렬

data = input()
result = []
sum = 0

for i in data:
    if i.isdigit:
        sum += str[i]
    else:
        result.append(i)

result.sort()
if sum != 0:
    result.append(str(sum))

#리스트를 문자열로 변환하여 출력
print(''.join(result))
