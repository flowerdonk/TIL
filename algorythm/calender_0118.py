import calendar

# 혼자 풀이
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

# 교수님 풀이

y_input = input('연도를 입력하시오 : ')

while calendar.isleap(y_input):
    print('윤년입니다. 연도를 다시 입력해주세요')
    y_input = input('연도를 입력하시오 : ')


print(calendar.calendar(y_input))

m_input = int(input('월을 입력하시오 : '))
d_input = int(input('일을 입력하시오 : '))
weekday_num = calendar.weekday(y_input, m_input, d_input)

if not weekday_num:
    print('경고 월요일입니다.')

week_dic = {0:'월요일', 1: '화요일', 2: '수요일', 3: '목요일', 4: '금요일', 5: '토요일', 6: '일요일'}

date_dict = {"년": y_input, "월": m_input, "일": d_input, "요일": week_dic[weekday_num]}

print(date_dict)