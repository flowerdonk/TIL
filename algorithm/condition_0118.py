# 1. 자연수 입력, 1부터 자연수까지 세로로 출력
num = int(input())

for i in range(num):
    print (i+1)

# 2. 자연수 입력, 1부터 자연수까지 가로로 출력
num = int(input())

for i in range(num):
    print (i+1, end = ' ')

# 3. 자연수 입력, 자연수부터 0까지 거꾸로 세로로 출력
num = int(input())

for i in range(num+1):
    print (num-i)

# 4. 자연수 입력, 자연수부터 0까지 거꾸로 가로로 출력
num = int(input())

for i in range(num+1):
    print (num-i, end = ' ')

# 5. 자연수 입력, 1부터 자연수까지의 합 출력 (10000이하)
num = int(input())
sum = 0
for i in range(num):
    sum += i+1

print(sum)

# 6. 자연수 입력, 높이가 자연수인 직각 삼각형 출력
num = int(input())

for i in range(num):
    for bl in range(num - i - 1):
        print(' ', end = '')
    for star in range(i+1):
        print('*', end = '')
    print('')

# 7. 중간값 찾기
numbers = [85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67, 51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24,]

numbers.sort()
print(numbers)

if len(numbers) % 2:
    print(numbers[len(numbers)//2])
else:
    print(numbers[len(numbers)/2 - 1])
