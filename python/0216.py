'''
def f(i, k, s, t): # i : 원소, k : 집합의 크기, s : i - 1까지 고려된 합, t : 목표
    global cnt
    global fcnt
    fcnt += 1

    if s > t: # 고려한 원소의 합이 찾는 합보다 큰 경우 되돌아감
        return

    if i == k: # 하나의 부분집합 완성
        if s == t:
            for j in range(k):
                if bit[j]:
                    print(A[j], end = ' ') # 합이 키인 부분집합을 출력
            print()
            cnt += 1
        return

    else:
        bit[i] = 1 # A[i] 원소를 부분집합에 포함시킴
        f(i + 1, k, s + A[i], t) # A[i] 포함
        bit[i] = 0
        f(i + 1, k, s, t) # A[i] 미포함

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(A)
key = 10
cnt = 0
bit = [0] * N
fcnt = 0 # 함수 호출된 횟수
f(0, N, 0, key) # 처음은 원소, 합이 0
print(cnt, fcnt) # 합이 key인 부분집합의 수
'''

'''
def f(i, k):
    if i == k:
        print(p)
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            # p[i] 결정, p[i]와 관련된 작업 가능
            f(i + 1, k)
            p[i], p[j] = p[j], p[i]


p = [1, 2, 3]
N = len(p)
f(0, N)

[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 2, 1]
[3, 1, 2]
'''

def Power(Base, Exponent):
    if Exponent == 0 or Base == 0:
        return 1
    
    if Exponent % 2 == 0:
        NewBase = Power(Base, Exponent/2)
        return NewBase * NewBase
    
    else:
        NewBase = Power(Base, (Exponent - 1)/2)
        return (NewBase * NewBase) * Base