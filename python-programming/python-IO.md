### 파이썬 입출력

> input()
>> 한줄의 문자열을 입력받음

> map()
>> 리스트의 모든 원소에 각각 특정한 함수를 적용할때 사용

    list(map(int, input().split()))
    
    n = int((input())
    # data = input().split() // 공백 기준으로 나눠서 문자열 형태로 리스트로 출력됨
    # a, b, c = map(int, input().split())
    data = list(map(int, input().split())) // 공백 기준으로 나눠서 int형으로 리스트로 출력됨
    
> 빠르게 입력받기 
>> sys.stdin.readline() 메서드 사용
>> 입력 후 엔터가 줄바꿈 기호로 입력됨으로 rstrip()메서드를 함께 사용함
>>  print(7, end=" ") // 줄바꿈 하지 않기 위해 end 사용 


> 정수형 데이터와 문자열 더하기 불가


    answer = 7
    print("정답은" + str(answer) )
    
