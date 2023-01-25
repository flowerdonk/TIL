from collections import Counter

entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']

entry = Counter(entry_record)
exit = Counter(exit_record)
entry_modified = entry.copy()
max_list = []

while len(max_list) != 3:
    max_num = 0
    max_name = ''
    for key in entry_modified:
        if entry_modified[key] >= max_num:
            max_num = entry_modified[key]
            max_name = key
    
    max_list.append([max_name, max_num])
    del entry_modified[max_name]

print('입장 기록 많은 Top3')
for item in max_list:
    print(f'{item[0]} {item[1]}회')

print('\n출입 기록이 수상한 사람')
for name in entry:
    if entry[name] != exit[name]:
        if entry[name] > exit[name]:
            print(f'{name}은 입장 기록이 {entry[name] - exit[name]}회 더 많아 수상합니다.')
        else:
            print(f'{name}은 퇴장 기록이 {exit[name] - entry[name]}회 더 많아 수상합니다.')


        
