# 두 도시 딕셔너리화, 리스트 내부 딕셔너리 내부 딕셔너리
air_info = [{'name': 'A', 'capital': True, 'air_status': {'O2': 3, 'CO2': 2}}, {'name': 'B', 'capital': False, 'air_status': {'O2': 5, 'CO2': 3}}]

# 산소 농도 값만을 모은 리스트 형성
O2_info = [air_info[0]['air_status']['O2'], air_info[1]['air_status']['O2']]
print(O2_info)