# 윤년 확인 (4의 배수 O and 100의 배수 X/400 배수)
while True:
    year = int(input())
    leap = 0

    if not year % 400:
        leap += 1
    else:
        if not year % 4:
            if year % 100:
                leap += 1

    if leap:
        print('윤년')
    else:
        print('평년')