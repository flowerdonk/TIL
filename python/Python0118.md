# 함수

1. **정의**

**1) Function**

특정한 기능을 하는 코드의 조각, 필요시에만 호출하여 간편히 사용

INPUT(parameters) → Docstring(function body) → OUTPUT(return)

print(list, end=’,’) → 리스트 값들 사이에 ‘,’ 추가

**2) 특징**

Decomposition : 기능을 분해, 재사용 가능하게 만듦

Abstraction : 복잡한 내용을 모르더라도 사용할 수 있도록, 재사용성, 가독성, 생산성

**3) 종류**

내장 함수 : 파이썬에 기본적으로 포함된 함수

외장 함수 : import 문을 통해 사용, 외부 라이브러리에서 제공
pip install / import requests / requests.get(’url’)

사용자 정의 함수 : 직접 사용자가 만드는 함수

- Void function
    
    명시적인  return 값 X, None을 반환하고 종료
    
    - 예시
        
        ```python
        def void_product(x, y):
            print(f'{x} x {y} = {x * y}')
        
        void_product(4, 5) # 4 x 5 = 20
        ans = void_product(4, 5) # 4 x 5 = 20
        print(ans) # None
        ```
        

- Value returning function
    
    return 문을 통해 값 반환, 값 반환 후 함수 바로 종료
    
    - 예시
        
        ```python
        def value_returning_product(x, y):
            return x * y
        
        value_returning_product(4, 5)
        ans = value_returning_product(4, 5)
        print(ans) # 20
        ```
        

1. **기본 구조**

선언, 호출(define & call) → 입력(input) → 문서화(docstring) → 범위(scope) → 결과값(output)

```
def function_name(parameter): # 함수는 parameter를 넘겨줄 수 있음
    '''
		docstring # 함수 body 앞에 선택적으로 작성, 반드시 첫 번째 문장에 문자열 ''''''
		'''
		# code block
    return returning_value # 동작 후에는 return을 통해 결과값을 전달, 반드시 하나의 값

function_name(argument) # 함수 호출
```

parameter → params / argument → args

**1) return으로 두 개 이상의 값 반환**

- 튜플 사용(컨테이너)
    
    ```python
    def fs(x, y):
        return x*y, x/y
    
    y = fs(4, 1)
    print(y) # (4, 4)
    print(type(y)) # <class 'tuple'>
    ```
    

**2) Argument**

함수 호출 시 함수의 parameter를 통해 전달되는 값

필수 Argument : 반드시 전달되어야 하는 Argument

선택 Argument : 값을 전달하지 않아도 되는 경우는 기본값이 전달

- Positional Argument
    
    기본적인 Argument, 위치에 따라 함수 내에 전달
    
    - 예시
        
        ```python
        def func(x, y):
            return x + y
        
        func(2, 3) # 값 직접 전달
        ```
        

- Keyword Argument
    
    직접 변수의 이름으로 특정 Argument 전달
    
    Keyword Argument 다음에 Positional Argument 활용 X → 반드시 Positional 먼저, 혹은 둘 다
    
    - 예시
        
        ```python
        def func(x, y):
            return x + y
        
        func(x = 2, y = 3) # x, y 둘 다 Keyword Argument
        func(2, y = 3) # y는 Keyword Argument
        func(x = 2, 3) # Error
        ```
        

- Default Arguments Values
    
    기본값 지정하여 함수 호출 시 argument 값 설정 X
    
    정의된 것 보다 더 적은 개수의 argument 들로 호출될 수 있음
    
    - 예시
        
        ```python
        def func(x, y = 0): # y는 Default Arguments Value
            return x + y
        
        func(2) # x에만 값 전달
        ```
        

1. **파이썬의 범위(Scope)**

**1) Namespace**

어떤 것을 할당했을 때 기억해두는 공간

**Built-in Namespace** : 기본적으로 장착되어 있는 공간, 매우 큼

**Global Namespace** : 하나의 파이썬 파일이 실행되면서 생성되는 공간

**Enclosing Namespace** : 함수가 중첩되어 있을 때, 바깥 함수의 네임스페이스

**Local Namespace** : 어떠한 함수를 실행하면, 함수 안 쪽에 생성되는 공간

- 예시
    
    ```python
    x = '글로벌' # global namespace
    
    def func1():
    		x = '인클로징' # Enclosing namespace
    
        def func2():
    				x = '로컬' # local namespace
            print(x)
    
    				print(locals()) # local namespace에 들어있는 요소 확인
    				print(globals()) # global namespace에 들어있는 요소 확인
    
    				global y # global variable 선언
    
        func2()
    
    func1()
    ```
    
    ```python
    x = '글로벌' 
    my_list = [1, 2, 3, 4]
    
    def func1():
        x = '로컬' # 중복된 이름의 새로운 x, 로컬에서만 작동하는 변수
        my_list[1] = 5 # 어떠한 이름을 갖고 있는 것이 X, my_list의 이름을 수정
    
    func1()
    print(x) # '글로벌'
    print(my_list) # [1, 5, 3, 4]
    ```
    
    ```python
    x = 1
    
    def func1():
        x = 2
    
        def func2():
            global x # func2 내부에서 사용하는 x는 global
            x = 3
            print(x) # 3 출력
    
        func2()
        print(x) # 2 출력, x는 로컬 먼저 확인
    
    func1()
    print(x) # 3 출력, func2에서 x값 수정됨
    
    # 3, 2, 3
    ```
    
    ```python
    def func1():
        x = 10
    
        def func2():
            nonlocal x # 자신을 감싸고 있는 가장 가까운 함수의 네임스페이스
            x = 20 # func1의 x 값(10)을 수정
    
        func2()
        print(x) # 20 출력
    
    func1()
    print(x) # Error, global에 x가 없음
    
    # 20 출력 후 Error
    ```
    

**2) Scope**

네임스페이스가 여러 개 있을 때, 접근하는 규칙을 정하는 것이 Scope 

내가 찾고자하는 변수의 위치에 접근하는 순서 : Local → Enclosing → Global → Built-in

함수 내에서 필요한 상위 scope 변수는 argument로 넘겨서 활용 (global, nonlocal 지양)

global scope : 코드 어디에서든 참조할 수 있는 공간

local scope : 함수가 만든 scope, 함수 내부에서만 참조 가능

- 예시
    
    ```python
    def func1():
        print('func1 start')
    
        def func2(): # 함수 내부의 함수
            print('func2 start')
            print('func2 end')
            return
    
        func2()
        return
    
    func1()
    ```
    

**3) Variable**

global variable : global scope에 정의된 변수

local variable : local scope에 정의된 변수

- 수명 주기
    
    built-in scope : 파이썬이 실행된 이후부터 영원히 유지
    
    global scope : 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
    
    local scope : 함수가 호출될 때 생성, 함수가 종료될 때까지 유지
    

1. **자주 쓰이는 함수**
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
    
- **map**
    
    
- join
    
    리스트를 문자열로 일정하게 합쳐주는 함수
    
    ```python
    ''.join(list_name) # ['a', 'b', 'c']를 'abc' 문자열로
    '구분자'.join(list_name) # 값 사이에 구분자를 합침
    ```
    
- get
    
    
-