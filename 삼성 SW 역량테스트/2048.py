#백준12100 2048(Easy)
#주어진 입력값에 따라 상하좌우값 더해서 최대값 구하는 알고리즘 
#
#
#

#1차시도 => 실패
from sys import stdin
from collections import deque

input = stdin.readline
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
#split() 활용해서 공백제거해서 인풋하기

#방향키 상하좌우
#최단거리? BFS

i = 0   #행부분 
j = 0   #열부분 
count = 0 
while count < 5:
  #print(a)

  if a[i][j] == a[i][j+1] : #열끼리 동일할경우
    tmp = int(a[i][j]*2)
    a[i][j+1]= tmp
    a[i][j] = 0 

    if i+1 == n : #리스트 오버플로우 방지
      count +=1 
      i = 0
    else :
      i+=1 
    continue 

  elif a[i][j] == a[i+1][j] : #행끼리 동일할경우
    tmp = int(a[i][j]*2)
    a[i+1][j] = tmp
    a[i][j] = 0 
    if j+1 == n :
      count +=1 
      j = 0
    else :
      j+=1 

    continue 
  else :
    #print("끝")
    break 

#print(a)
print(max(max(a)))
