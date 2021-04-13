#백준18222 투에-모스 문자열 
#
#
#
#

#2차시도 시간초과 
from sys import stdin

n = int(stdin.readline()) 

answer = '01'
tmp = 2 
while True :
  for i in range(tmp) :
    if answer[i] == '0' :
      answer += '1'
    else :
      answer += '0'

  if tmp < n :
      tmp = tmp ** 2
  else :
    print(answer[n-1])
    break

#1차시도 시간초과
from sys import stdin
import math

n = int(stdin.readline()) 

answer = '01'
tmp = 2 

for i in range(n) :
  for j in answer :
    if j == '0' :
      answer += '1'
    else :
      answer += '0'

print(answer[n-1])










