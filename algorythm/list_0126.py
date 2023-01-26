
# sample_list = [11, 22, 33, 55, 66]

# # 주어진 리스트의 3번 index에 있는 항목 제거, 변수에 할당

# print("original list: ", sample_list)

# value = sample_list.pop(3)
# print("list after: ", sample_list, "\nvalue: ", value)

# # 가장 뒤에 77 추가
# sample_list.append(77)
# print("add list: ", sample_list)

# # value 값을 2번 인덱스에 추가
# sample_list.insert(2, value)
# print("value add list: ", sample_list)

# my_tuple = (11, 22, 33, 44, 55, 66)

# # 주어진 튜플에서 44와 55의 값을 새로운 튜플에 할당
# new_tuple = (my_tuple[3], my_tuple[4])
# print(new_tuple)

# original_list = [1, 2, 3]
# copy_list = original_list
# print(original_list, copy_list) # [1, 2, 3] [1, 2, 3]

# copy_list[0] = 'hello'
# print(original_list, copy_list) # ['hello', 2, 3] ['hello', 2, 3]

# a = [1, 2, ['a', 'b']]
# b = a[:]
# print(a, b) # [1, 2, ['a', 'b']] [1, 2, ['a', 'b']]
# b[2][0] = 0
# print(a, b) # [1, 2, [0, 'b']] [1, 2, [0, 'b']]

# import copy

# a = [1, 2, ['a', 'b']]
# b = copy.deepcopy(a)

# print(a, b) # [1, 2, ['a', 'b']] [1, 2, ['a', 'b']]

# b[2][0] = 0
# print(a, b) # [1, 2, ['a', 'b']] [1, 2, [0, 'b']]

# scores = [('eng', 88), ('sci', 90), ('math', 80)]

# # 정렬
# scores.sort() # 각 원소의 맨 앞 값 기준으로 정렬
# print(scores) # [('eng', 88), ('math', 80), ('sci', 90)]

# scores.sort(key = lambda x:x[1]) # 1번째 인덱스 값대로 정렬
# print(scores) # [('math', 80), ('eng', 88), ('sci', 90)]

a = 257
b = 257

c = 'hello'
d = 'hello'

print(c is d) # True
print(id(c)) # 2201851921392
print(id(d)) # 2201851921392
print(a is b) # True

list_a = [1, 2, 3, 4, 5]
list_b = list_a # 얕은 복사
temp = []