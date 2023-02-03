def Area(Rects):
    area = 0
    paper = [[0 for _ in range(101)] for _ in range(101)]

    for i in range(4):
        x1 = Rects[i][0]
        y1 = Rects[i][1]
        x2 = Rects[i][2]
        y2 = Rects[i][3]

        for j in range(x1, x2):
            for r in range(y1, y2):
                paper[j][r] = 1

    for row in paper:
        area += sum(row)

    return area


Rects = [] # 왼쪽아래 x, y, 오른쪽 위 x, y
for i in range(4):
    Rects.append(list(map(int, input().split())))

print(Area(Rects))