'''
def BFS(G, v): # 그래프 G, 탐색 시작점 v
    visited = [0] * (n + 1) # n : 정점의 개수
    queue = [] # 큐 생성
    queue.append(v) # 시작점 v를 큐에 삽입
    visited[v] = 1

    while queue: # 큐가 비어있지 않은 경우
        t = queue.pop(0) # 큐의 첫번째 원소 반환
        visit(t) # 정점 t에서 할 일

        for i in G[t]: # t와 연결된 모든 정점에 대해
            if not visited[i]: # 방문되지 않은 곳이라면
                queue.append(i) # 큐에 넣기
                visited[i] = visited[n] + 1 # n으로부터 1만큼 이동


while front != rear:
    pass

while Q:
'''

'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

1번 시작
거리 순 분류 : 1 - 1 / 2 - 2, 3 / 3 - 4, 5, 7 / 4 - 6
간선 순서대로 나열 : 1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7
출력 결과 예시 : 1-2-3-4-5-7-6
'''
def bfs(v, N): # 시작점, 마지막 정점 번호
    visited = [0] * (N + 1) # visited 생성
    q = [v] # Queue 생성(시작점 인큐)
    visited[v] = 1 # 시작점 인큐 표시(visited)

    while q: # 큐가 비어있지 않으면
        t = q.pop(0) # dequeue
        print(t, end = ' ') # t에서 처리할 일 
        
        for v in adjL[t]: # t에 인접
            if visited[v] == 0: # 방문한 적 없는 v
                q.append(v) # v 인큐
                visited[v] = visited[t] + 1 # 인큐되었음 표시

    print() 
    print(visited) # [0, 1, 2, 2, 3, 3, 4, 3]

V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjL = [[] for _ in range(V + 1)] # 1번부터 V번까지, 연결정보

for i in range(E):
    n1, n2 = arr[i * 2], arr[i * 2 + 1]
    # 방향이 없으므로 양쪽 모두 해야함
    adjL[n1].append(n2)
    adjL[n2].append(n1)

bfs(1, V) # 1번부터 마지막 정점 V 탐색 순서 찍기