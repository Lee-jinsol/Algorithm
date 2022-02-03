### 파이썬 함수 

> 내장함수
>> 만약 전역변수랑 지역변수 변수명을 똑같이 선언하면 지역변수가 우선시됨 

> 사용자 정의 함수

    a = 0 
    array = [1,2,3,4]
    
    def 함수명(매게변수):
      global a ( 밖에 전역변수로 선언이 되어있어야함) 초기화 해도 됨 a = 0 이렇게
      array.append(6)
      return 리턴값
      
 ----
 
 > 람다 표현식 
 >> 여러개의 리스트에 동일하게 적용하고 싶은게 있을때


     def add(a.b):
      return a+b
      
     print(lambda a,b:a+b(3,7))
     
    array = [('홍길',50),('순신',32),('무개',70)] //array안에 튜플로 되어있음 
     
    # 적은 나이를 먼저 
    def key(x):
      return x[1]
    
    print(sorted(array, key=key)) 
    print(sorted(array, key=lambda x:x[1])) //람다 써서 한줄로 처리도 가능함 왜냐면 키함수는 한번 쓰이고 안쓰이는거니까 람다 사용하는게 좋음
    
    map 각각에 원소에 어떠한 함수를 적용하고자 할떄
    result = map(lambda a,b:a+b, list1,list2)
    //a랑 b가 주어졌을때 a와b를 더하는 함수를 정의하고 a와b에는 list1, list2를 대입
    
----
## 표준 라이브러리
    
> itertools
>> 순열과 조합라이브러리는 코테에서 자주 사용

> heapq
>> 우선 순위 큐 기능을 구현하기 위해 자주 사용

> bisect coolections maths

> sum(), min(), max(), eval(), sorted()//기본이 오름차순, 
---- 
> 순열 ( from itertools import permutations )
> 중복 순열 ( from itertools import product )
>> 서로다른 n개에서 서로다른 r개를 선택하여 일렬로 나열하는것 

    result = list(permutations(data,3))

> 조합 ( from itertools import combinations )
> 중복 조합 ( from itertools import combinations_with_replacement )
>> 서로다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는것

 
