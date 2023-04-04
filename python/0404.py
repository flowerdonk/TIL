'''
# findset()
def find_set(x): # x가 속한 대표 원소 리턴
    while x != rep[x]: # x == rep[x]가 될 때까지
        x = rep[x]
    return x

# union()
def union(x, y): # y의 대표 원소가 x의 대표 원소를 가리키도록 함
    rep[find_set(y)] = find_set(x)

    # rep[y] = find_set(x) 
    # -> 잘못됨. 자기 자신을 가리키는 대표원소의 연결을 바꿔야함 그렇지 않으면 연결이 끊기게 됨


# makeset()
rep = [i for i in range(6)]
'''

'''
입력 예시)
마지막 정점 번호, 11개의 간선
정점 정보, 가중치
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)

V, E = map(int, input().split()) # 0 ~ V: 정점번호, E: 간선 수
rep = [i for i in range(V + 1)]
graph = []

for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph.append([v1, v2, w])

# [1] 가중치 기준 오름차순 정렬
graph.sort(key=lambda x:x[2])

# [2] N개의 정점(V + 1)에 대해서, N - 1개의 간선 선택
N = V + 1
s = 0 # MST에 포함된 간선의 가중치 합
cnt = 0 # 선택
MST = []
for u, v, w in graph: # 가중치가 작은 것부터
    # 두 개의 대표 원소를 찾고 비교
    if find_set(u) != find_set(v): # 사이클이 생기지 않으면
        cnt += 1
        s += w # 가중치 합
        MST.append([u, v, w])
        union(u, v)
        if cnt == N - 1: # MST 구성 완료
            break

print(s) # 175
print(MST) # [[3, 5, 18], [1, 2, 21], [2, 6, 25], [0, 2, 31], [3, 4, 34], [2, 4, 46]]
'''

'''
입력예시)
정점 번호, 간선 개수
5 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''
def dijkstra(s, V):        # s: 출발, v: 마지막 정점 번호
    U = [0] * (V + 1)      # 최소 비용이 결정된 정점 집합
    U[s] = 1               # U = {s}

    for i in range(V + 1): # s에서 나머지 정점 i로 가는 비용
        D[i] = adjM[s][i]

    # while U != V: 남은 정점 비용 결정
    N = V + 1              # N개의 정점
    for _ in range(N - 1): # N - 1개 정점의 비용 결정
        # D[w]가 최소인 w 결정
        minV = INF
        w = 0
        for i in range(V + 1):
            # 비용이 확정되지 않은 원소(남은 정점 i) 중 최소
            if U[i] == 0 and minV > D[i]:
                w = i
                minV = D[i]
        U[w] = 1            # 최소인 w는 비용 확정
        
        # w에 인접인 정점에 대해, 기존비용 vs w를 거쳐가는 비용 비교
        for v in range(V + 1):
            # w에 인접인 v의 조건: 자기자신, 무한 값 제외 
            if 0 < adjM[w][v] < INF:
                D[v] = min(D[v], D[w] + adjM[w][v])


INF = 10000                             # 문제에 따라 다름
V, E = map(int, input().split())        # 0 ~ V: 정점, E: 간선 수
adjM = [[INF] * (V + 1) for _ in range(V + 1)]
for i in range(V + 1):
    adjM[i][i] = 0                      # 자기자신으로 가는 비용
for _ in range(E):
    u, v, w = map(int, input().split()) # u -> v, w: 가중치
    adjM[u][v] = w

D = [0] * (V + 1)
dijkstra(0, V)
print(D) # [0, 2, 3, 9, 6, 10]