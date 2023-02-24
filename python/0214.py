# def fibo(n):
#     global memo
#     if n >= 2 and memo[n] == 0:
#         memo[n] = (fibo(n - 1) + fibo(n - 2))
#         return memo[n]

# memo = [0] * (n + 1) # memo를 위한 배열 할당, 모두 0으로 초기화
# memo[0] = 0
# memo[1] = 1

# def fibo(n):
#     f = [0] * (n + 1)
#     f[0] = 0
#     f[1] = 1

#     for i in range(2, n + 1):
#         f[i] = f[i - 1] + f[i - 2]

#     return f[n]

# def f(i, k):
#     if i == k: # 목표에 도달
#         print(B)
#         return
#     else:
#         B[i] = A[i]
#         f(i + 1, k)

# A = [10, 20, 30]
# # A = [i for i in range(1000)] # RecursionError 재귀 최대 깊이를 넘어섬
# B = [0] * 3
# f(0, 3)

# visited[], stack[] 초기화

# DFS(v)
#     시작점 v 방문
#     visited[v] <- True
    
#     while {
#         if (v의 인접 정점 중 방문 안 한 정점 w가 있으면)
#             push(v)
#             v <- w (w에 방문)
#             visited[w] <- True
        
#         else:
#             if (스택이 비어 있지 않으면)
#                 v <- pop(stack)
#             else:
#                 break
#     }
# end DFS()

# '''
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# '''
# V, E = map(int, input().split())
# arr = list(map(int, input().split()))
# adjM = [[0] * (V + 1) for _ in range(V + 1)]
# for _ in range(E):
#     v1, v2 = arr[i * 2], arr[i * 2 + 1]
#     adjM[v1][v2] = 1
#     adjM[v2][v1] = 1
