def Card(N, A_list, B_list):
    result = []

    for i in range(N):
        num_A = A_list[i][0]
        num_B = B_list[i][0]

        # 0 - 세모, 1 - 네모, 2 - 동그라미, 3 - 별
        shape_A = [0] * 4
        shape_B = [0] * 4
        for r in range(1, num_A + 1):
            shape_A[A_list[i][r] - 1] += 1
        for r in range(1, num_B + 1):
            shape_B[B_list[i][r] - 1] += 1

        for i in range(3, -1, -1): # 그림 비교 별 -> 세모
            if shape_A[i] > shape_B[i]:
                result.append('A')
                break
            elif shape_A[i] < shape_B[i]:
                result.append('B')
                break
            else:
                if i != 0:
                    continue
                else:
                    result.append('D')
                    break

    return result


N = int(input())
A_list = []
B_list = []

for i in range(N):
    A_list.append(list(map(int, input().split())))
    B_list.append(list(map(int, input().split())))

result = Card(N, A_list, B_list)
for i in range(N):
    print(result[i])



""" 입력
# 4 - 별, 3 - 동그라미, 2 - 네모, 1 - 세모
5               테스트 케이스 수
1 4             A/그림 1개/ 별1
4 3 3 2 1       A/그림 4개/ 동그라미2, 네모1, 세모1 
5 2 4 3 2 1     A/
4 4 3 3 1       A/
4 3 2 1 1       A/
4 2 3 2 1       B/
4 4 3 2 1       B/
3 4 3 2         B/
5 4 4 2 3 1     B/
5 4 2 4 1 3     B/
"""

""" 출력
# 승자 출력, D - 무승부
라운드별 승자
"""