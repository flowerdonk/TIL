'''
N = 10
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            print(i, j, k)

def nCr(n, r, s):
    if r == 0:
        print(comb)
    else:
        for i in range(s, n - r + 1):
            comb[r - 1] = A[i]
            nCr(n, r - 1, i + 1)
'''

'''
n = 5
r = 3
comb = [0] * 3
A = [i for i in range(1, n + 1)]
nCr(n, r, 0)
'''

def f(i, k):            # bit[i]를 결정하는 함수
    if i == k:          # bit의 모든 원소 결정
        print(*bit)
    else:
        bit[i] = 0      # 해당 자리가 0일 때
        f(i + 1, k)
        bit[i] = 1      # 해당 자리가 1일 때
        f(i + 1, k) 


A = [7, 2, 5, 3, 4]
N = len(A)
bit = [0] * N           # bit[i] : A[i] 원소가 부분집합에 포함되는지 여부
