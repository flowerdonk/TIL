'''
def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output, end = ' ')

a = 0x10
x = 0x01020304

print("%d = " %a, end = '')
Bbit_print(a)
print()
print("0%X = " %x, end = '')
for i in range(0, 4):
    Bbit_print((x >> i * 8) & 0xff)

16 = 00010000 
01020304 = 00000100 00000011 00000010 00000001
'''

'''
import sys

print(sys.byteorder)

def ce(n) : # change endian
    p = []
    for i in range(0, 4):
        p.append((n >> (24 - i * 8)) & 0xff)
    return p

x = 0x01020304
p = []
for i in range(0, 4):
    p.append((n >> (24 - i * 8)) & 0xff)

print("x = %d%d%d%d" %(p[0], p[1], p[2], p[3]))
p = ce(x)
print("x = %d%d%d%d" %(p[0], p[1], p[2], p[3]))

def ce1(n):
    return (n << 24 & 0xff000000) | (n << 8 & 0xff0000) \
        | (n >> 8 & 0xff00) | (n >> 24 & 0xff)

def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output)

a = 0x86
key = 0xAA

print("a           ==> ", end = '')
Bbit_print(a)

print("a^ = key    ==> ", end = '')
a ^= key
Bbit_print(a)

print("a^ = key    ==> ", end = '')
a ^= key
Bbit_print(a)

a           ==> 10000110
a^ = key    ==> 00101100
a^ = key    ==> 10000110
'''

'''
01D06079861D79F99F

arr = input()
for x in arr:
    num = int(x, 16) # 16진수임을 밝히고 정수로 변환
    for j in range(3, -1, -1):
        bit = 1 if num & (1 << j) else 0
        print(bit, end = '')
    print(' ', end = '')

0000 0001 1101 0000 0110 0000 0111 1001 1000 0110 0001 1101 0111 1001 1111 1001 1001 1111  
'''

'''
arr = input()

for i in range(len(arr)):
    tmp = int(arr[i], 16) # 10진수로 바꾸고

# 10진수에서 2진수로 바꾸기
# tmp = 0 -> tmp = 0000

tmp = bin(tmp).replace('0b', '')

while len(tmp) != 4:
    tmp = '0' + tmp

print(tmp) # 1111

'''