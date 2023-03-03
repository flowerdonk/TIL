N, M = input().split() # 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M
N = int(N)
M = int(M)

N_set = set()
M_set = set()

for i in range(N):
    N_set.add(input()) # 듣도 못한 사람의 이름

for i in range(M):
    M_set.add(input()) # 보도 못한 사람의 이름

NM_list = list(N_set & M_set)
NM_list.sort()

print(len(NM_list)) # 듣보잡의 수 출력
for i in range(len(NM_list)):
    print(NM_list[i]) # 명단을 사전순 출력

