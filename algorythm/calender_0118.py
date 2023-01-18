import calendar

leap = 1
days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]

while leap:
    year = int(input('연도를 입력하시오 : '))
    if calendar.isleap(year):
        print('윤년입니다. 연도를 다시 입력해주세요')
    else:
        leap = 0

print(calendar.calendar(year))

month = int(input())
day = int(input())
dayname = calendar.weekday(year, month, day)
if dayname == 0:
    print('경고 월요일입니다.')
print(f"{{'년': {year}. '월': {month}, '일': {day}, '요일': '{days[dayname]}'}}")