'''1. 
x, y = 10, 20

temp = x
x = y
y = temp

print(x, y)
'''


'''2. 
a = []
b = []
c = a # c에 a의 주솟값을 줌(참조)

print(id(a))
print(id(b))
print(id(c))

result = (a is b)
print(result)

result = (a is c)
print(result)
'''

'''3. 
result = True

if result:
    print('확인')
'''

'''4.
list_a = []
list_b = [1, 2, 3]
list_c = list()

#list[]       0          1                      2
list_d = [[1, 2, 3], ['python'], ['서울', '대전', '부울경', '구미']]
#list[][]  0  1  2       0          0       1       2        3
'''

'''5. 
boxes = ['A', 'B', ['apple', 'banana', 'cherry']]

print(len(boxes)) # 3
print(boxes[2]) # ['apple', 'banana', 'cherry']
print(boxes[2][-1]) # cherry, '-'는 역순
print(boxes[-1][1][0]) # b, ['apple', 'banana', 'cherry']에서 'banana'의 0번째 원소
'''

'''6.
print(list(range(1, 10, 2))) #스텝 (시작, 10까지, 2씩 커지게)

print(list(range(6, 1, -1))) #역순 (시작, 1까지, 1씩 작아지게)
'''

'''7. 
# 리스트 슬라이싱, 0부터 4까지(4 미포함) 2씩 증가
print([1, 2, 3, 4][0:4:2]) # [1, 3]

# 튜플 슬라이싱
print((1, 2, 3, 4, 5)[0:4:2]) # [1, 3]

# 문자열 슬라이싱
print('abcdefhg'[1:4:2]) # [b, d]
'''

'''8.
dict_a = {'a': 'apple', 'b' : 'banana'}
print(dict_a['c']) # KeyError, 실행 X
dict_a.get('c') # 매칭되는 key 값이 없음, None return

result = dict_a.get('c')
if not result:
    print('값 없음.')
'''

'''9.
print('3' + 4) # TypeError
print(int('3') + 4) # 7

print('3.5' + 3.5) # TypeError
print(float('3')) # 3.0
'''

'''10.
s = '이것은 문자열입니다.'
print(id(s)) 
s = '이것은 문자열?' # 문자열 재할당
print(id(s)) # 앞선 메모리 주소와 다름

num = 10
print(id(num))
num = 15 # 변수 메모리 재할당
print(id(num)) # 앞선 메모리 주소와 다름
'''

'''hws1.
score = {
    'python': 80,
    'django': 89,
    'web': 83
}

score['algorithm'] = 90
score['python'] = 85

print(sum(score.values())/4)
'''

'''hws2.
s = input('숫자를 입력해주세요 : ')
s = map(int, list(s))
print(sum(s))
'''

'''hws3.
'''
#1. 
print("It's SSAFY 8")

#2. 
print(458345 + 623576)

#3.
greeting = 'Hello'
month = 'July'

print(greeting + ' ' + month)

#4.
hello = input()
print(hello)