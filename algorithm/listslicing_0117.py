# 총 15대의 배가 있는 항구, 배가 있으면 T, 배가 없으면 F

ports = [False] * 15
ports[3] = True
ports[7] = True
ports[8] = True
ports[14] = True
print(ports)

# 홀수 선착장 정보
odd_ports = ports[0 : 15 : 2] # range 스텝과 동일하게, list에도 슬라이싱
print(odd_ports)