# Python

# 변수, 식별자, 연산자

1. **변수**

동일 변수에 다른 데이터를 언제든 할당(저장)할 수 있음

추상화 : 코드 가독성 증가, 수정 용이

할당 연산자(=)를 통해 값을 할당
같은 값 동시 할당 가능, 다른 값 동시 할당 가능
값 설정 없이 메모리만 우선 할당할 경우 value = None

- 예시
    
    ```python
    # 01 중요!
    x, y = 10, 20
    
    temp = x
    x = y
    y = temp
    
    print(x, y)
    
    ///////////////////////////////////////////////////////////////////////
    
    # 02
    x, y = 10, 20
    
    y, x = x, y
    print(x, y)
    ```
    

1. **식별자**

변수의 이름, 읽기 쉽고 이해하기 쉽게

- 변수 이름 규칙
    
    식별자 이름은 영문 알파벳, 언더스코어(_), 숫자로 구성
    
    첫 글자에 숫자 X
    
    길이 제한 X, 대소문자 구별
    
- 사용 불가 키워드(예약어)
    
    ’False’, ‘None’, ‘True’, ‘__peg_parser__’, ‘and’, ‘as’, ‘assert’, ‘async’, ‘await’, ‘break’, ‘class’, ‘continue’, ‘def’, ‘del’, ‘elif’, ‘else’, ‘except’, ‘finally’, ‘for’, ‘from’, ‘global’, ‘if’, ‘import’, ‘in’, ‘is’, ‘lambda’, ‘nonlocal’, ‘not’, ‘or’, ‘pass’, ‘raise’, ‘return’, ‘try’, ‘while’, ‘with’, ‘yield’
    
    → 사용 변수 삭제 키워드 del value_name
    

1. **주석**

# → 한 줄 짜리 주석

“”” “”” → 여러 줄 짜리 주석

1. **연산자**

| 연산자 | + | - | * | ** | / | // |
| --- | --- | --- | --- | --- | --- | --- |
| 내용 | 덧셈 | 뺄셈 | 곱셈 | 거듭제곱 | 나눗셈 | 몫 |

우선순위 : 곱하기(*), 나누기(/)가 더하기(+), 빼기(-)보다 먼저 계산

- 복합연산자
    
    연산과 할당을 합쳐놓음
    
    +=, -=, *=, /=
    

# 자료형

1. **메모리**

데이터 10을 컴퓨터가 기억하는 과정

1️⃣ 10을 저장할 공간을 메모리에 형성
2️⃣ 저장할 공간에 대한 주소를 할당
3️⃣ 할당 받은 주소를 기억
4️⃣ 10이라는 데이터를 해당 주소로 찾아가 저장
5️⃣ 이후 10이 필요해지면 해당 주소로 가서 읽어옴

주소값을 기억하기 힘들기 때문에 기억하기 쉬운 이름으로 바꾸는 것 ⇒ **변수**
자료형마다 차지하는 메모리 크기가 다름 - **id(변수)**를 통해 주소값 확인 가능

- 예시
    
    ```python
    s = '이것은 문자열입니다.'
    print(id(s)) 
    s = '이것은 문자열?' # 문자열 재할당
    print(id(s)) # 앞선 메모리 주소와 다름
    
    num = 10
    print(id(num))
    num = 15 # 변수 메모리 재할당
    print(id(num)) # 앞선 메모리 주소와 다름
    ```
    

1. **자료형 분류**

| 진수 | 2진수 (binary) | 8진수 (octal) | 16진수 (hexadecimal) |
| --- | --- | --- | --- |
| 표현 | 0b | 0o | 0x |
- **수치형 (Numeric Type)**
    
    **1) int (정수) : 일반적인 수학 연산 가능**
    
    절댓값 : abs()
    
    **2) float (실수, 부동소수점) : 유리수, 무리수 포함 실수**
    
    실수 연산의 경우 의도하지 않은 값이 나올 수 있음 (3.2 - 3.1 ≠ 1.2 - 1.1)
    
    반올림 : round(값, 소수점자릿수)
    0~4는 내림, 짝수에서 5는 내림 / 홀수에서 5는 올림
    
    **3) complex (복소수)**
    
- **문자열 (String Type)**
    
    모든 문자는 str 타입, 작은따옴표(’)나 큰따옴표(”) 활용
    Str = char타입의 연속적인 배열, 순서가 있는 시퀀스형 자료형
    
    삼중 따옴표 : 여러 줄을 나눠 입력할 때 편리
    
    문자열 연산 : 덧셈 (”A” + “B” = “AB”),  곱셈 (”A” * 3 = “AAA”)
    
    String Interpolation : 문자열을 변수로 활용
    
    print(f’문자열{변수} ~ {변수}문자열’)
    
    input() → 무조건 스트링
    
- **불린형 (Boolean Type)**
    
    논리 자료형, 참과 거짓(True, False)을 표현 → 비교/논리 연산에서 활용
    
    0 → false, 1 → true
    
    falsy 값 = (), [], {}, None, …
    
    **1) 비교 연산자**
    
    | 비교 연산자 | <, > | <=, >= | ==, != | is, is not |
    | --- | --- | --- | --- | --- |
    | 내용 | 미만, 초과 | 이하, 이상 | 같음, 같지 않음 | OOP O, X |
    - 예시
        
        ```python
        a = []
        b = []
        c = a # c에 a의 주솟값을 줌(참조)
        
        print(id(a)) # a 주솟값
        print(id(b)) # b 주솟값
        print(id(c)) # c 주솟값 = a 주솟값
        
        result = (a is b)
        print(result) # False 출력
        
        result = (a is c)
        print(result) # True 출력
        ```
        
        ```python
        result = True
        
        if result:
            print('확인') # 정상 출력
        ```
        
    
    **2) 논리 연산자**
    
    | 논리 연산자 | A and B | A or B | Not |
    | --- | --- | --- | --- |
    | 내용 | A, B 모두 True 
    → True | A, B 모두 False 
    → True | True를 False로,
    Fasle를 True로 |
    
    우선순위 : not, and, or 순 (괄호 사용 필수)
    
- **컨테이너**
    
    분류 : 순서가 있는 데이터 (Ordered) vs 순서가 없는 데이터 (Unordered)
    
    순서가 있다 ≠ 정렬되어 있다
    
    **1) list : list_name = [], a = list()**
    
    가변형, 시퀀스형
    
    어떤 자료형도 저장 가능, 리스트 안에 리스트 저장도 가능 → 유연성
    
    순서가 있는 시퀀스, 인덱스(0부터 시작)를 통해 접근 가능 list_name[index]
    
    순회 가능한(iterable) 자료형, 빈 리스트 → false
    
    여러개 원소를 가진 리스트 생성 listname = [ ] * 15
    
    리스트 슬라이싱 → 슬라이싱할리스트[ 처음 : 끝 : 슬라이싱 단위 ]
    
    - 예시
        
        ```python
        list_a = []
        list_b = [1, 2, 3]
        list_c = list()
        
        #list[]       0          1                      2
        list_d = [[1, 2, 3], ['python'], ['서울', '대전', '부울경', '구미']]
        #list[][]  0  1  2       0          0       1       2        3
        ```
        
        ```python
        boxes = ['A', 'B', ['apple', 'banana', 'cherry']]
        
        print(len(boxes)) # 3
        print(boxes[2]) # ['apple', 'banana', 'cherry']
        print(boxes[2][-1]) # cherry, '-'는 역순
        print(boxes[-1][1][0]) # b, [~]에서 'banana'의 0번째 원소
        ```
        
        ```python
        # 리스트 곱하기로 형성
        ports = [False] * 15
        ports[3] = True
        ports[7] = True
        ports[8] = True
        ports[14] = True
        print(ports)
        
        #[False, False, False, True, False, False, False, True, True, False, False, False, False, False, True]
        
        # 홀수 선착장 정보
        odd_ports = ports[0 : 15 : 2] # range 스텝과 동일하게, list에도 슬라이싱
        print(odd_ports)
        ```
        
    
    **2) tuple : tuple_name = (), a = tuple()**
    
    불변형, 시퀀스형
    
    수정 불가능한 시퀀스, 인덱스로 접근 가능 tuple_name[index]
    
    단일 항목의 경우, 값 뒤에 쉼표를 붙여야 함 tuple_a = (1, ) 혹은 1,
    
    복수 항목의 경우, 마지막 항목에 쉼표는 권장
    
    **3) range : range(n), range(n, m)**
    
    불변형, 시퀀스형
    
    기본형 : range(n) → 0부터 n-1까지의 숫자 시퀀스
    
    범위 지정 : range(n, m) → n부터 m-1까지의 숫자 시퀀스
    
    스텝 : 일정한 크기로 증감
    
    - 예시
        
        ```python
        # 스텝
        print(list(range(1, 10, 2))) # (시작, 10까지, 2씩 커지게)
        
        print(list(range(6, 1, -1))) #역순 (시작, 1까지, 1씩 작아지게)
        ```
        
    
    **4) dict : dict_name = {'key1':'value1’, 'key2':'value2’}, a = dict()**
    
    가변형, 비시퀀스형, 순회 가능한(iterable) 자료형
    
    키-값 쌍으로 이루어진 자료형, key값을 통해 value에 접근이 가능
    
    key : 변경 불가능한 데이터만 활용 가능 (string, int, float, bool, tuple, range)
    
    value : 어떤 형태든 가능
    
    - 예시
        
        ```python
        dict_a = {'a': 'apple', 'b' : 'banana'}
        print(dict_a['c']) # KeyError, 실행 X
        dict_a.get('c') # 매칭되는 key 값이 없음, None return
        
        result = dict_a.get('c')
        if not result:
            print('값 없음.')
        ```
        
        ```python
        score = { 'a': 80, 'b': 89, 'c': 83 }
        
        score['a'] = 90 # key를 통해 value 값 수정
        score['d'] = 85 # 원소 추가
        
        sum(score.values())/len(score.values()) # value 값의 합 / 길이
        ```
        
    
    **5) set : set_name = set([ ]) or set(’ ’), s = set()**
    
    가변형, 비시퀀스형
    
    중복 X, 순서 X → 인덱싱 지원 X, 인덱스로 접근하기 위해서는 리스트나 튜플로 변환
    
    교집합 : s1 & s2 or s1.intersection(s2)
    
    합집합 : s1 | s2 or s1.union(s2)
    
    차집합 : s1 - s2 or s1.difference(s2)
    
    - 예시
        
        ```python
        # 복권 당첨 확인
        ssafy_choice = set([1, 12, 27, 33, 38, 42])
        lucky_numbers = set([7, 15, 27, 33, 37, 42])
        countlist = ssafy_choice & lucky_numbers
        count = len(countlist)
        print(count)
        ```
        
    
- **None**
    
    일반적으로 반환 값이 없는 함수에서 사용하는 타입, 값이 없음을 표현
    

1. **Escape sequence (제어 시퀀스)**

| 예약 
문자 | \n | \t | \r | \0 | \\ | \’ | \” |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 내용
(의미) | 줄 바꿈 | 탭 | 캐리지
리턴 | 널
(Null) | \ | 단일인용 | 이중인용 |

1. **형변환**
- **암시적 형변환 (Implict)**
    
    사용자가 의도하지 X, 파이썬 내부적으로 자료형 변환
    
    bool : True(1), False(0)
    
    Numeric type : 3 + 5.0 = 8.0
    
- **명시적 형변환 (Explicit)**
    
    사용자가 특정 함수를 활용하여 의도적으로 자료형을 변환
    
    단, 형식에 맞는 문자열만 정수로 변환 가능
    
    - 예시
        
        ```python
        print('3' + 4) # TypeError
        print(int('3') + 4) # 7
        
        print('3.5' + 3.5) # TypeError
        print(float('3')) # 3.0
        
        print(str(1)) # 1
        print(str([1, 2, 3]) # [1, 2, 3]
        ```
        

1. **슬라이싱**

[시작 : 끝(미포함) : range]

인덱스, 콜론을 사용하여 문자열의 특정 부분만 잘라낼 수 있음

콜론을 기준으로 앞 인덱스에 해당하는 문자는 포함, 뒤 인덱스는 미포함

[  : 끝] → 시작부터 특정 위치까지 가져오기

[ 시작 :  ] → 특정 인덱스부터 끝까지 가져오기

- 예시
    
    ```python
    # 리스트 슬라이싱, 0부터 4까지(4 미포함) 2씩 증가
    print([1, 2, 3, 4][0:4:2]) # [1, 3]
    
    # 튜플 슬라이싱
    print((1, 2, 3, 4, 5)[0:4:2]) # [1, 3]
    
    # 문자열 슬라이싱
    print('abcdefhg'[1:4:2]) # [b, d]
    ```
    

# 제어문

순차, 선택, 반복

파이썬은 기본적으로 위에서부터 아래로 차례대로 명령 수행

1. **조건문**
- **if, else**
    
    참/거짓을 판단할 수 있는 조건식과 함께 사용
    
    ```python
    if '조건' == True:
        # code block
    else:
        # code block
    ```
    
    - 예시
        
        ```python
        num = int(input())%2
        if num: # 0이 아닌 모든 수는 True
            print('홀수')
        else:
            print('짝수')
        ```
        
- **복수 조건문 elif**
    
    ```python
    if '조건':
        # code block
    elif '조건':
        # code block
    else:
        # code block
    ```
    
    - 예시
        
        ```python
        dust = int(input())
        
        if dust > 150:
            print('\n매우 나쁨!')
        elif dust > 80:
            print('\n나쁨!')
        elif dust > 30:
            print('\n보통!')
        else:
            print('\n좋음!')
        
        print('\n미세먼지 확인 완료')
        ```
        
        ⇒ 조건식은 동시에 검사하는 것이 아니라 순차적으로 비교!
        
- **중첩 조건문**
    
    if 안에 if, 들여쓰기에 유의
    
    ```python
    if '조건':
        # code block
        if '조건':
            # code block
    else:
        # code block
    ```
    
    - 예시
        
        ```python
        if dust > 150:
            print('\n매우 나쁨!')
            if dust > 300:
                print('\n실외 활동을 자제하세요.')
        ```
        
- **4) 조건 표현식**
    
    삼항 연산자라고 부르기도 함.
    
    ‘true인 경우 값’ if ‘조건’ else ‘false인 경우 값’
    → value = num if num >= 0 else -num
    
    - 예시
        
        ```python
        num = int(input())
        result = '홀수' if num % 2 else '짝수'
        print(result)
        ```
        

1. **반복문**
- **while**
    
    조건이  True라면 무한 반복, 반드시 종료 조건을 필요로 함
    
    ```python
    while '조건':
        # code block
    ```
    
    - 예시
        
        ```python
        a = 0
        
        while a < 5:
            print(a)
            a += 1
        
        print('끝') # 반복 종료 시 출력
        ```
        
- **for**
    
    순회 가능한 자료형(iterable) 내에서 반복
    
    리스트 등에서 원소 가져오기 가능, 종료 조건이 별도 필요 X
    
    ```python
    for '변수' in iterable:
        # code block
    ```
    
    - 순회가능 자료형 (string, list, dict, tuple, range, set etc…)
        - 예시
            
            ```python
            dusts = [59, 24, 102] # list 순회
            for i in dusts:
                print(i)
            ```
            
            ```python
            chars = input() # string 순회
            
            for char in chars:
                print(char)
            ```
            
            ```python
            chars = input()
            
            for idx in range(len(chars)): # 숫자로 순회
                print(chars[idx]) # 인덱스가 필요
            ```
            
            ```python
            apbs = {'a' : 1, 'b' : 2, 'c' : 3} # dict 순회
            
            for apb in apbs: # 기본적으로 key로 순회
                print(apb)
            
            for apb in apbs:
                print(apb, apbs[apb]) # key와 value 함께 출력
            ```
            
            - 추가 메서드를 활용한 딕셔너리 순회
                
                keys() : key로 구성
                
                values() : value로 구성
                
                items() : (key, value)의 튜플로 구성
                
                ```python
                apbs = {'a' : 1, 'b' : 2, 'c' : 3}
                print(apbs.keys()) # dict_keys(['a', 'b', 'c'])
                print(apbs.values()) # dict_values([1, 2, 3])
                print(apbs.items()) # dict_items([('a', 1), ('b', 2), ('c', 3)])
                
                for apb, apbs in apbs.items():
                    print(apb, apbs)
                ```
                
    
    - 순회형 함수(range, enumerate)
        
        ```python
        enumerate(iterable, start = 0) # start 인덱스 설정 가능
        ```
        
        - 예시
            
            ```python
            apbs = ['a', 'b', 'c'] 
            for idx, apb in enumerate(apbs): # enumerate
                print(idx, apb)
            # 0 a
            # 1 b
            # 2 c
            ```
            
    
    - List Comprehension
        
        표현식, 제어문을 통해 특정한 값을 가진 리스트를 생성
        
        ```python
        [code for '변수' in iterable]
        [code for '변수' in iterable in '조건식']
        ```
        
        - 예시
            
            ```python
            cubic_list = [number ** 3 for number in range(1, 4)]
            print(cubic_list) # [1, 8, 27]
            ```
            
    
    - Dictionary Comprehension
        
        표현식, 제어문을 통해 특정한 값을 가진 딕셔너리를 생성
        
        ```python
        {key:value for '변수' in iterable}
        {key:value for '변수' in iterable in '조건식'}
        ```
        
        - 예시
            
            ```python
            cubic_dict = {number: number ** 3 for number in range(1, 4)}
            print(cubic_dict) # {1: 1, 2: 8, 3: 27}
            ```
            
- **반복 제어**
    - break : 반복문을 벗어남(종료)
    - continue : 해당 반복문을 건너뛰고, 다음 반복
    - for-else : 끝까지 반복문을 실행한 이후에 else 문 실행
        
        break를 통해 중간에 종료되는 경우, else 문 실행 X
        
    - pass : 아무것도 하지 않음, 이후 추가할 내용 공백 메꿈

# Html

- **API** **요청&응답**
    
    요청(주소 url) → 응답(문서 html)
    API : 두 소프트웨어가 통신(요청&응답)하도록 연결해주는 인터페이스
    
    ```python
    import requests #터미널에서 python -m pip install requests 선행 필수
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1021'
    response = requests.get(url).json()
    ```
    
    ```python
    response = {'totSellamnt': 101960162000, 'returnValue': 'success', 'drwNoDate': '2022-06-25', 'firstWinamnt': 2108962250, 
    'drwtNo6': 45, 'drwtNo4': 24, 'firstPrzwnerCo': 12, 'drwtNo5': 29, 'bnusNo': 16, 'firstAccumamnt': 25307547000, 
    'drwNo': 1021, 'drwtNo2': 15, 'drwtNo3': 17, 'drwtNo1': 12}
    ```
    
    동일
    
    ```python
    print(response.get('drwtNo1'))
    print(response.get('drwtNo2'))
    print(response.get('drwtNo3'))
    print(response.get('drwtNo4'))
    print(response.get('drwtNo5'))
    print(response.get('drwtNo6'))
    ```
    
    ```python
    for i in range(1, 7):
        number = f'drwtNo{i}'
        print(response.get(number))
    ```
    
    동일
    

# 함수

- 정의
    
    def
    
- 출력
    
    print(list, end=’,’) → 리스트 값들 사이에 ‘,’ 추가
    
- **랜덤**
    
    ```python
    import random
    
    menu = ['양자강', '순남시래기', '싸밥']
    
    lunch = random.choice(menu)
    print(f'오늘 점심 메뉴는{lunch}') #f"", f'' 둘 다 가능
    ```
    
    ```python
    import random
    
    numbers = range(1, 45)
    
    lucky_number = random.sample(numbers, 6) #개수만큼 뽑기, random.sample(리스트, 개수)
    print(f'행운의 숫자는 : {lucky_number}입니다.')
    ```
    
- map
    
    

# 단축어

alt+shift → 문장 복사

alt+방향키 → 문장 이동

ctrl+shift+l → 같은 단어 찾기

alt+ctrl+방향키 → 문장 복수 선택

하이라이트 신택스 : 텍스트 색상 → 가독성

#