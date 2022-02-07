#공백을 기준으로 두 수 입력받기 
n,k = map(int, input().split()) #map 함수를 이용해서 각각 int형으로 바꿈

result = 0

while True:
    target  = (n // k)* k
    result += (n - target)
    n = target

    if n<k:
        break
     
    result += 1
    n //= k


result += (n-1)
print(result)




