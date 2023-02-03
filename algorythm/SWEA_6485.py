import sys
sys.stdin = open('input.txt')

def Bus(T, N, lineA, P, lineN):
    count = [0] * 5001

    for i in range(N):
        for j in range(lineA[i][0] - 1, lineA[i][1]):
            count[j] += 1

    return count[:P]

'''
입력

T 테스트 케이스 수
N 버스 노선 개수
Ai Bi 버스 노선 번호 범위 (Ai <= bus <= Bi)
...
P 버스 정류장 개수
Cj j번째 정수는 Cj번 버스 정류장을 지나는 버스 노선의 개수
...
'''
T = int(input())
result = []
for i in range(T):
    N = int(input())
    lineA = []
    for i in range(N):
        lineA.append(list(map(int, input().split())))
    P = int(input())
    lineN = []
    for i in range(P):
        lineN.append(int(input()))
    result.append(Bus(T, N, lineA, P, lineN))
    

'''
출력

각 정류장에 몇 개의 버스 노선이 다니는지
'''
for i in range(T):
    print(f'#{i + 1}', *result[i])