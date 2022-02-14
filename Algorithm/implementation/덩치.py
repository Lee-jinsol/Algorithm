#키 몸무게 (x,y)
n = int(input())
a = []
result = []



for i in range(n):
    a.append(list(map(int,input().split())))
for j in range(n): 
    sum = 0
    for k in range(n): 
        if a[j][0] < a[k][0] and a[j][1] < a[k][1]:
            sum += 1
    result.append(sum+1)
           
for i in result:
    print(i, end=" ")

'''
a[0][0] > a[1][0] d
a[0][1]> a[1][1]

a[0][0] a[1][0] a[2][0]
a[0][1] a[1][1]

[0][0] [0][1] [1][1]
'''
