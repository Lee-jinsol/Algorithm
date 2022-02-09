# 곱하기 혹은 더하기 문제 

# 수가 0이나 1인경우 더한다
# 두수가 모두 2이상인 경우에 곱한다

data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)