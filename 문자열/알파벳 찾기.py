#백준10809 알파벳찾기
#소문자의 알파벳에 대한 인덱스 찾기 
#
#string 라이브러리 활용!! + 딕셔너리-리스트-문자열 변환
#

import string

dicted = { i : -1 for i in string.ascii_lowercase }

idx = 0
num = input()
for n in num :
    if dicted[n] == -1 :
        dicted[n] = idx
    idx += 1

tmp = list(dicted.values())
answer = " ".join(str(i) for i in tmp)
print(answer)
