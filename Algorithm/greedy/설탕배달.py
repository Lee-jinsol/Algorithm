
    suger = int(input())
    result = 0
    multi = 0
    rangeCoin = suger // 3

    if (suger % 5) == 0 :
        result = suger // 5
    else :
        for i in range (rangeCoin):
            multi = suger -(3*(i+1))
            result += 1
            if (multi % 5) == 0:
                result += (multi//5)
                multi = 0
                break
        if multi != 0:
            result = -1
        
    print(result)

'''
suger = int(input())
result = 0

while suger > 0:
    if (suger % 5) == 0:
        result += suger // 5
        suger = 0
        break
    suger -= 3
    result += 1

if suger != 0:
    result = -1


print(result)
'''