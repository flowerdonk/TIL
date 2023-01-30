pillarN = int(input())
store = [] * 1000
input_pillar = []
input_pillar.append(list(map(int, input().split())))

for i in range(pillarN):
    store[input_pillar[i][0]] = input_pillar[i][1]

