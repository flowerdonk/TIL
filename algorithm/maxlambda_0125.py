grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500), ('토란',1300)]

max_num = 0
max = ''

for grain in grain_lst:
    if grain[1] >= max_num:
        max_num = grain[1]
        max = grain[0]

print(max)

# 교수님 풀이 - 람다 함수

grain_lst.sort(key = lambda x : x[1], reverse=True) # 내림차순
print(grain_lst[0][0])

# 교수님 풀이 - 딕셔너리, 리스트

grain_dict = dict(grain_lst)
grain_keys = list(grain_dict.keys())
grain_prices = list(grain_dict.values())

print(grain_keys[grain_prices.index(max(grain_prices))])