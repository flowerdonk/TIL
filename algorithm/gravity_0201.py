'''
총 26개 상자
회전 후 중력 작용, 낙차가 가장 큰 상자의 낙차 리턴
상자의 위치는 2차원, 모두 벽에 붙어있음
방의 길이는 100 * 100, 즉 상자는 0~100 높이로 쌓을 수 있음

* 입력
총 시도 횟수
개수
상자높이(순서대로)
-> 반복

* 출력
#1 최대 낙차 값
...
'''
# # 자신의 위치보다 뒤에있는 수 중에, 같거나 큰 수가 몇개인지
# # 같거나 큰 수가 많을수록 낙차는 작아짐 - 많이 쌓이기 때문

def Gravity(total_N, width, box_list):
    total = []
    for num in range(total_N):
        fall = []
        for i in range(len(box_list[num])):
            count = 0

            for after in box_list[num][i + 1:]:
                if box_list[num][i] == 0:
                    break

                if box_list[num][i] <= after:
                    count += 1

            fall.append(width[num] - count - i - 1)
        total.append(max(fall))
    return total

total_N = int(input())
width = []
box_list = []
for i in range(total_N):
    width.append(int(input()))
    box_list.append(list(map(int, input().split())))

for i in range(total_N):
    print(f'#{i+1} {Gravity(total_N, width, box_list)[i]}')
