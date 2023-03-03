'''
def road(v):
    visited[v] += 1
    ans.append(v)

    for w in range(1, V + 1):
        # if len(arr[w]) == 0:
        #     return
        # 지금 현재 정점 -> 다음으로 갈 정점 가능 여부 체크
        if w in arr[v] and visited[w] == 0:
            road(w)

    return ans


T = 10
V = 100
for n in range(1, T + 1):
    _, E = map(int, input().split())
    data = list(map(int, input().split()))

    visited = [0] * (V + 1)
    arr = [[] * (V + 1) for _ in range(V + 1)]

    for i in range(E):
        n1, n2 = data[i * 2], data[i * 2 + 1]
        arr[n1].append(n2)

    ans = []
    rst = 1 if road(0).count(99) >= 1 else 0
    print(f'#{n} {rst}')
'''
import sys
sys.stdin = open('input.txt')

def dfs(v):
    ans.append(v)
    visited[v] = 1
    if v == 99:
        return 0

    for n in arr[v]:
        if visited[n] == 0:
            if dfs(n) == 0:
                return 0

T = 10
for tc in range(1, T + 1):
    _, N = map(int, input().split())
    data = list(map(int, input().split()))
    arr = [[] for _ in range(100)]

    for i in range(N):
        idx = data[i * 2]
        val = data[i * 2 + 1]
        arr[idx].append(val)

    visited = [0] * 100
    ans = []
    dfs(0)
    if ans.pop() == 99:
        print(1)
    else:
        print(0)
