'''
def enq(n):
    global last
    last += 1           # 완전 이진트리에 마지막 정점 추가
    heap[last] = n      # 마지막 정점에 저장
    c = last            # 부모가 있고, 부모 > 자식 -> 조건 검사
    p = c // 2          # 완전 이진 트리여서, 소숫점 버림

    while p > 0 and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p           # 옮긴 자리에서 부모와 비교하기 위해 (부모 위치에서 부모를 또 찾음)
        p = c // 2

    return

def deq():
    global last
    tmp = heap[1]       # 루트 임시저장
    heap[1] = heap[last]# 마지막 정점의 값을 루트로 이동
    last -= 1           # 마지막 정점 삭제
    p = 1
    c = p * 2           # 왼쪽 자식 번호

    while c <= last:    # 자식이 하나 이상 있으면

        # 오른쪽 자식도 있고, 오른쪽 자식의 키가 더 크면
        if c + 1 <= last and heap[c] < heap[c + 1]:
            c += 1      # 비교 대상을 오른쪽 자식으로 변경

        # 자식이 부모보다 크면
        if heap[c] > heap[p]:
            heap[c], heap[p] = heap[p], heap[c]
            p = c
            c = p * 2
        else:
            break

    return tmp

heap = [0] * 101        # 완전 이진트리 1번 - 100번 인덱스 준비
last = 0                # 완전 이진트리의 마지막 정점 번호

enq(5)
print(heap[1])          # 5
enq(15)
print(heap[1])          # 15
enq(8)
print(heap[1])          # 15
enq(20)
print(heap[1])          # 20

while last > 0:
    print(deq())

'''

N = 6
data = [3, 6, 2, 1, 7, 9]
tree = [0 for _ in range(N + 1)]
last = 1
parent = child = 0

for i in range(len(data)):
    if not tree[i]:             # 아무것도 기록되지 않았으면
        tree[last] = data[i]    # 데이터를 넣어줌
    else:
        last += 1
        child = last            # 새로 추가된 정점을 자식으로
        parent = child // 2     # 완전 이진 트리에서 부모 정점 번호를 구해줌

        tree[child] = data[i]
        # print(tree, child, parent)

    # 부모가 있고, 부모가 자식보다 큰 동안 (부모가 작아질 때까지)
    while parent >= 1 and tree[parent] > tree[child]:
        # 부모와 자식 위치를 변경
        tree[parent], tree[child] = tree[child], tree[parent]
        # 자식 위치를 부모로 변경
        child = parent
        parent = child // 2

print(tree)