import sys
sys.stdin = open('input.txt')

def gravity(boxes):
    max = 0
    for n in range(len(boxes)):
        next = 0
        for box in boxes[n + 1:]:
            if box >= boxes[n]:
                next += 1
        diff = len(boxes) - n - next - 1
        if max <= diff:
            max = diff

    return max

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    boxes = list(map(int, input().split()))

    print(f'#{i} {gravity(boxes)}')