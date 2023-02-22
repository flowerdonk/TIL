import sys
sys.stdin = open('input.txt')

def solution(n):
    answer = []
    input_s = list(map(int, input().split()))
    result = [[input_s[i + j - 1] for j in range(i)] for i in range(1, n + 1)]
    print(result)
    arr = [[] * n for _ in range(n)]

    direction = [[1, 0], [0, 1], [-1, -1]] # 아래, 오른쪽, 대각선 왼쪽 위

    for num in range(len(result)): # arr에 입력받은
        pass


    return answer

T = 3
for tc in range(1, T + 1):
    n = int(input())
    print(solution(n))