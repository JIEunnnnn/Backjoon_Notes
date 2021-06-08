#백준2908 상수 
#주어진 입력값을 뒤집어, 최대값 구하는 문제
#
#문자열 특징[::-1] + 음의무한대
#

import math

alpha = list(input().split())
answer = -math.inf

for a in alpha :
    tmp = int(a[::-1])
    if answer < tmp :
        answer = tmp

print(answer)

