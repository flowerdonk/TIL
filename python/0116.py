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