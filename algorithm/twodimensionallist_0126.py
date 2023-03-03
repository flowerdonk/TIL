my_list1 = []
my_list2 = []

N, M = map(int, input().split())

for i in range(N):
    my_list1.append(list(map(int, (input().split()))))

for i in range(N):
    my_list2.append(list(map(int, (input().split()))))

sum_list = []
for i in range(N):
    sum_list.append([])
    for r in range(M):
        sum_list[i].append(my_list1[i][r] + my_list2[i][r])

for i in range(N):
    for r in range(M):
        print(sum_list[i][r], end =' ')
    print('')
