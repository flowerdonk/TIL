'''
트리 정점 총 수 V, 간선 V - 1
간선은 항상 ‘부모’ ‘자식’ 순서로 표기
간선은 부모 정점 번호로 오름차순, 부모 정점이 동일하다면 자식 정점 번호로 오름차순 나열

v = 13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

c1 = [] # 왼쪽 자식 노드
c2 = [] # 오른쪽 자식 노드

def pre(i):
    if i > 0:
        print(i)
        pre(c1[i])
        pre(c2[i])