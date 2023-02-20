import sys
sys.stdin = open('input.txt')

def code(arr):
    cnt = 1

    while cnt: # 0 이하 발생 시 반복문 종료
        for n in range(1, 6): # 5씩 싸이클
            fst = arr.pop(0) # 맨 앞 변수에 할당

            if fst - n <= 0: # 감소한 수가 0 이하일 때
                arr.append(0) # 0 삽입
                cnt = 0 # 반복문 종료
                break

            else:
                arr.append(fst - n) # 감소한 수 삽입

T = 10
for i in range(1, T + 1):
    _ = input()
    arr = list(map(int, input().split()))
    code(arr)
    
    print(f'#{i}', *arr)