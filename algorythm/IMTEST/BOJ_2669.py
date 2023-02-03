def Area(Rects):
    area = 0
    Rects.sort(key = lambda x : x[0])
    
    return area


Rects = [] # 왼쪽아래 x, y, 오른쪽 위 x, y
for i in range(4):
    Rects.append(list(map(int, input().split())))

print(Area(Rects))