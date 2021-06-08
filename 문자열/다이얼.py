#백준5622 다이얼
#전화번호에 따른, 최소 시간구하는 문제
#
#처음에, 딕셔너리 정의할때, 번호 4개있는 것 고려 X 
#문제를 제대로 보자!!

import string

dial = {}
tmp = 2
flag = True
for s in string.ascii_uppercase :
    if s == 'S' :
        dial[s] = tmp
        tmp +=1
        cnt = 0
        flag = False
        continue

    if flag :
        if (ord(s) - 65) % 3 == 0:
            tmp += 1
        dial[s] = tmp
    else :
        dial[s] = tmp
        cnt += 1
        if cnt > 2 :
            cnt = 0
            tmp += 1


dial['Z'] = dial['Y']

num = input()
count = 0

for n in num :
    count += dial[n]

print(count)


