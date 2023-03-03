import sys
sys.stdin = open('input.txt')

def nod(S):
    visited[S] = 1
    ans.append(v)

    for w in range(1, V + 1):
        if arr[S][w] == 1 and visited[w] == 0:
            nod(w)

    return visited

T = 10
for m in range(1, T + 1):
    V, E = map(int, input().split()) # 노드 수, 간선 수
    nodes = list(map(int, input().split()))
    visited = [0] * (V + 1)

    arr = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        n1, n2 = nodes[i]
        arr[n1][n2] = 1

    ans = []

    for l in range(V):
        if len(nod(l)) == V:
            a = nod(l)

    print(f'#{n} {a}')