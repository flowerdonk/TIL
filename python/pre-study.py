# count = int(input())
# num = [count][9]

# for i in range(count):
#     for r in range(10):
#         input(num[i][r])
#     num[i].sort()

# for i in range(count):
#     print(f'#{i+1} {num[i][9]}')

# for i in range(count):
#     num[i] = input().split(' ')
#     num[i] = list(map(int, num))
#     num[i].sort()
#     print(f'#{i} {num[i][9]}')

# line = int(input())
# num = [line-1]

# for i in range(line):
#     num[i] = str(input()).split(' ')
#     num[i] = list(map(int, num))
#     num[i].sort()

# for i in range(line):
#     print(f'#{i} {num[i][9]}')

# T = int(input())
# big = [0]
# for i in range(T):
#     num = list(map(int,input().split()))
#     big.append(max(num))

# for i in range(T):
#     print(f'#{i+1} {big[i+1]}')

T = int(input())
big = [0]
for i in range(T):
    num = list(map(int,input().split()))
    result = round(sum(num)/10)
    big.append(result)

for i in range(T):
    print(f'#{i+1} {big[i+1]}')