import sys
sys.stdin = open('input.txt')

def palindrome(arr):
    mx = []
    for i in range(N):
        for x in range(N): # 가로 판별
            for n in range(N - 1, x - 1, -1):
                length = 0
                word1 = arr[i][x:n+1]
                if arr[i][x] == arr[i][n] and word1[::] == word1[::-1]:
                    length = n - x + 1
                    mx.append(length)
        for y in range(N): # 세로 판별
            for n in range(N - 1, y - 1, -1):
                length = 0
                word2 = ''
                for c in range(y, n + 1):
                    word2 += arr[c][i]
                if arr[y][i] == arr[n][i] and word2[::] == word2[::-1]:
                    length = n - y + 1
                    mx.append(length)

    return max(mx)

T = 10
N = 100
for i in range(1, T + 1):
    _ = input()
    arr = [input() for _ in range(N)]
    print(f'#{i} {palindrome(arr)}')
