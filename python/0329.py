'''
def merge(left, right):
    pass

def msort(m):
    if len(m) == 1:
        return m
    middle = len(m) // 2

    left = m[0:middle]
    right = m[middle:]

    left = msort(left)
    right = msort(right)

    return merge(left, right)

T =  int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    msort(arr)
'''

'''
'''
import sys
sys.stdin = open('input.txt')

def msort(s, e):
    if s == e:
        return
    m = (s + e) // 2
    msort(s, m)
    msort(m + 1, e)

    k = 0
    l, r = s, m + 1 # 왼쪽과 오른쪽에서 가장 작은 숫자의 위치

    while l <= m or r <= e:
        if l <= m and r <= e:
            if arr[l] <= arr[r]:
                temp[k] = arr[l]
                l += 1
            else:
                temp[k] = arr[r]
                r += 1
            k += 1
        elif l <= m: # l이 남아있는 상태라면
            while l <= m:
                temp[k] = arr[l]
                l += 1
                k += 1
        elif r <= e: # r이 남아있는 상태라면
            while r <= e:
                temp[k] = arr[r]
                r += 1
                k += 1
    
    i = 0
    while i < k:
        arr[s + i] = temp[i]
        i += 1

    return

N = 1000000
arr = list(map(int, input().split()))
temp = [0] * N # 합칠 때 임시 저장하는 용도
msort(0, N - 1)
print(arr[500000])

# def hoare(A, l, r):     # 파티셔닝
#     pivot = A[l]        # 가장 왼쪽 원소 기준
#     i = l               # 피봇보다 큰 값을 찾아 오른쪽으로 이동
#     j = r               # 피봇보다 작은 값을 찾아 왼쪽으로 이동

#     while i <= j:       # 교차하지 않은 상태
#         while i <= j and A[i] <= pivot: # 피봇보다 큰 원소를 만나거나 교차하면 멈춤
#             i += 1
#         while i <= j and A[j] >= pivot: # 피봇보다 작은 원소를 만나거나 교차하면 멈춤
#             j -= 1
#         if i < j:       # 교차하지 않은 경우
#             A[i], A[j] = A[j], A[i]

#     # 교차했을 경우
#     A[j], A[l] = A[l], A[j]
#     return j

# def qsort(A, l, r):
#     if l < r:
#         s = hoare(A, l, r)
#         qsort(A, l, s - 1)
#         qsort(A, s + 1, r)


# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())    # 100만개가 넘는 값
#     arr = list(map(int, input().split()))
#     qsort(arr, 0, N - 1)