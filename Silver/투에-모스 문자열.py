#백준18222 투에-모스 문자열 
#
#
#
#

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










