#소마 대비문제
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
n_list.sort()

def binarysearch(k, n_list, start, end):
    if start > end:
        return 0
    middle = (start +end) // 2
    if k == n_list[middle]:
        return 1
    elif k < n_list[middle]:
        return binarysearch(k, n_list, start, middle-1)
    else:
        return binarysearch(k, n_list, middle+1, end)

for k in m_list:
    start = 0
    end = len(n_list)-1
    print(binarysearch(k, n_list, start, end))