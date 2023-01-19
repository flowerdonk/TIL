# 함수의 응용

1. **함수의 활용**

**1) 내장 함수 (Built-in Functions)** 

[Python Built-in Functions](https://docs.python.org/3/library/functions.html)

- map (function, iterable)
    
    순회 가능한 데이터구조의 모든 요소에 함수를 적용하고, 그 결과를  map object로 반환
    
    - 예시
        
        ```python
        def func(n):
            return n * 10
        
        my_list = [1, 2, 3, 4, 5]
        
        map_obj = map(func, my_list)
        
        print(list(map_obj)) # 맵 오브젝트를 리스트에 담기
        # [10, 20, 30, 40, 50]
        ```
        
        ```python
        n, m = map(int, input().split()) # split을 통해 iterable로 변함
        
        print(n, m)
        print(type(n), type(m)) # <class 'int'> <class 'int'>
        ```
        
- filter(function, iterable)
    
    순회 가능한 데이터구조의 모든 요소에 함수를 적용하고, 그 결과가 True인 것들을 filter object로 반환
    
    - 예시
        
        ```python
        def odd(n):
            return n % 2
        
        numbers = [1, 2, 3]
        
        result = filter(odd, numbers)
        
        print(list(result)) # [1, 3]
        print(type(result)) # <class 'filter'>
        ```
        
- zip(*iterables)
    
    복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환
    
    - 예시
        
        ```python
        girls = ['jane', 'achley']
        boys = ['justin', 'eric']
        
        pair = zip(girls, boys)
        
        print(list(pair)) # [('jane', 'justin'), ('achley', 'eric')]
        print(type(pair)) # <class 'zip'>
        ```
        
- lambda[parameter] : 표현식
    
    lambda 매개변수 : 매개변수를 이용한 리턴값
    
    익명 함수, 표현식을 계산한 결괏값을 반환하는 함수
    
    다시 쓸 일이 없는 함수, 일회성 함수가 필요할 때 사용
    
    return문을 가질 수 X, 간편 조건문 외 조건문, 반복문 X
    
    간결하게 함수를 사용 가능, def를 사용하지 못하는 곳에서 사용 가능
    
    - 예시
        
        ```python
        print((lambda x : x * x)(4)) # 16, 실행을 위해서는 (람다)(값)
        
        my_func = lambda n : n * 2 # 변수에 람다함수 할당 가능
        print(my_func(2)) # 4
        
        map_obj = map(lambda x : x * x, [1, 2, 3])
        rlt = list(map_obj)
        print(rlt) # [1, 4, 9]
        ```
        
- 재귀 함수
    
    자기 자신을 호출하는 함수, 계산은 가장 마지막부터 시작
    
    무한한 호출을 목표 X, 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
    
    1개 이상의 base case(종료되는 상황)가 존재, 수렴하도록 작성
    
    멈추기 위해 break 사용 X → break는 반복문에서 사용
    
    메모리 스택이 넘치면 동작 X → stack overflow
    최대 재귀 깊이는 1,000번, 넘으면 → Recursion Error
    
    - 예시
        
        ```python
        def factorial(n):
            if n == 0 or n == 1: # base case, 종료 조건
                return 1
            else:
                return n * factorial(n-1)
        
        print(factorial(5)) # 120
        # 계산 순서 1 * 2 * 3 * 4 * 5
        ```
        
- 랜덤
    
    random 임포트 필수
    
    - 예시
        
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
        
- join
    
    리스트를 문자열로 일정하게 합쳐주는 함수
    
    - 예시
        
        ```python
        ''.join(list_name) # ['a', 'b', 'c']를 'abc' 문자열로
        '구분자'.join(list_name) # 값 사이에 구분자를 합침
        ```
        
- get
    
    

**2) 함수 가변 입력 (패킹/언패킹)**

- ***** → 패킹/언패킹 연산자
    
    모든 시퀀스형(리스트, 튜플 등)은 패킹/언패킹 연산자 * 를 사용해 객체의 패킹/언패킹 가능
    
    함수 파라미터에 가변 인자를 사용 가능하게 해줌
    
    ```python
    # packing
    a, b = 1, 2, 3, 4 # ValueError
    a, *b = 1, 2, 3, 4 # a = 1, b = (2, 3, 4), 남은 값을 묶어서 모두 할당
    
    # unpacking
    def my_sum(a, b, c):
        return a + b + c
    
    num_list = [10, 20, 30]
    
    rlt = my_sum(*num_list) # 60, 리스트 요소 각각 나눠서 들어감
    ```
    
    - 예시
        
        ```python
        def test(*values): # 남는 것 모두 들어갈 수 있음 -> 가변 인자 사용 가능
            for value in values:
                print(value)
        
        test(1) # 1
        test(1, 2) # 1, 2
        test(1, 2, 3, 4) # 1, 2, 3, 4
        ```
        
        ```python
        def my_sum(a, *agrs): # 값 하나는 필수, 이후 다른 것들은 모두 패킹
            rlt = 0
            for value in agrs:
                rlt += value
            return rlt
        
        my_sum() # Error 인자 하나는 필수
        my_sum(1, 2, 3) # 6
        ```
        
- 가변 키워드 인자(**kwargs)
    
    parameter에 **를 붙여 표현, 몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때 유용
    
    **kwargs는 딕셔너리로 묵여 처리 → 키워드는 ‘key’로, 값은 ‘value’로
    
    - 예시
        
        ```python
        def test(**kwargs): # 키워드 인자가 들어오면, 몇 개를 넣던 간에 접근 가능
            print(kwargs, type(kwargs))
            kwargs['name']
            return kwargs
        
        test(name = 'aiden', age = 21)
        
        def test(*args, **kwargs): # keyword는 kwargs에, 나머지는 모두 args에
            print(kwargs, type(kwargs))
            kwargs['name']
            return kwargs
        
        test(1, 2, 3, 4, name = 'aiden', age = 21) # args = 1, 2, 3, 4
        ```
        

**3) 모듈, 패키지**

- 모듈
    
    특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것
    
    다양한 함수를 묶어 하나의 파일로 만든 것
    
    import module / from module import var, function, Class / from module import *
    

- 패키지
    
    여러 모듈을 묶어 하나의 폴더로 만든 것
    
    특정 기능과 관련된 여러 모듈의 집합
    
    패키지 안에는 또 다른 서브 패키지를 포함
    
    from package import module / from package.module import var, function, Class
    
    ![하나의 패키지 calc 안에 모듈 tools를 바깥의 모듈에서 사용하는 방법
    __init__.py 는 아무 내용이 없어도 됨](%E1%84%92%E1%85%A1%E1%86%B7%E1%84%89%E1%85%AE%E1%84%8B%E1%85%B4%20%E1%84%8B%E1%85%B3%E1%86%BC%E1%84%8B%E1%85%AD%E1%86%BC%20025fb3a8061b4e16a8c0fd4196e12d8e/Untitled.png)
    
    하나의 패키지 calc 안에 모듈 tools를 바깥의 모듈에서 사용하는 방법
    __init__.py 는 아무 내용이 없어도 됨
    

- 라이브러리
    
    다양한 패키지를 묶어 하나의 폴더로 만든 것
    

- pip
    
    이것을 관리하는 관리자
    
    bash, cmd 환경에서 사용
    
    최신 버전 설치 : $ pip install SomePackage
    특정 버전 설치 : $ pip install SomePackage == 1.0.5
    최소 버전 설치 : $ pip install SomePackage >= 1.0.4
    
    패키지 삭제 : $ pip uninstall SomePackage
    
    패키지 목록 : $ pip list
    
    패키지 정보 : $ pip show SomePackage
    
    - 패키지 관리하기
        
        명령어들을 통해 패키지 목록을 관리, 설치 가능
        
        일반적으로 패키지를 기록하는 파일의 이름은 requirements.txt로 정의
        
        패키지 관리 : $ pip freeze > requirements.txt
        
        패키지 설치 : $ pip install > requirements.txt
        

- 가상환경
    
    패키지의 활용 공간
    

**4) 가상환경**

복수의 프로젝트를 하는 경우 버전이 상이할 수 있기 때문에, 가상환경 형성 후 독립적인 패키지 관리