#백준2675 단어공부
#주어진 문자열 중에서 가장 많이 나온 알파벳 찾기 
#
#딕셔너리 + max 메소드 활용
#

import string

dicted = {i : 0 for i in string.ascii_uppercase }

alpha = input()
for a in alpha :
    tmp = a.upper()
    if tmp in dicted :
        dicted[tmp] += 1


max_values = max(dicted.values())
answer = []
for i,v in dicted.items() :
    if v == max_values :
        answer.append(i)
        if len(answer) > 1 :
            answer[0] = "?"
            break

print(answer[0])
