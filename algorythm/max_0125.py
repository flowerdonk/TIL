grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500), ('토란',1300)]

max_num = 0
max = ''

for grain in grain_lst:
    if grain[1] >= max_num:
        max_num = grain[1]
        max = grain[0]

print(max)