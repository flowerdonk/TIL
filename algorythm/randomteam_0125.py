import random

members = [
'조현기', '최예훈', '배희진', '조재웅', '박영서', '김동준', '엄한결', '정준혁',
'김동욱', '연제정', '서인덕', '정예륜', '이명우', '고세훈', '김유진', '김동훈', 
'고서영', '김연재', '유진욱', '김영석', '김솔', '류나연', '이현도', '하재우', 
'김재석', '황재천', '박도현', '임휘진'
]
lunch = []
select = ''

for i in range(7):
    select_list = []
    for r in range(4):
        select = random.choice(members)
        select_list.append(select)
        members.remove(select)

        if r == 3:
            lunch.append(select_list)

for i in range(7):
    print(lunch[i])
