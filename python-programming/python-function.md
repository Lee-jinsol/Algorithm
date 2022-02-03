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


     def add(a.b):
      return a+b
      
     print(lambda a,b:a+b(3,7))
     
    array = [('홍길',50),('순신',32),('무개',70)] //array안에 튜플로 되어있음 
     
    # 적은 나이를 먼저 
    def key(x):
      return x[1]
    
    print(sorted(array, key=key)) 
    print(sorted(array, key=lambda x:x[1])) //람다 써서 한줄로 처리도 가능함 왜냐면 키함수는 한번 쓰이고 안쓰이는거니까 람다 사용하는게 좋음
    
