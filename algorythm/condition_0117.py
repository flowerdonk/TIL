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

#동일 문제
year = int(input('연도를 입력해주세요!'))

if ((year % 4 == 0)and (year % 100 != 0)) or (year % 400 ==0):
    print('윤년')
else:
    print('평년')