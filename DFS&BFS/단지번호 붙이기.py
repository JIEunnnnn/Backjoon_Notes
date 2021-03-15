#백준2667 단지번호붙이기
#몇단지가 몇가구씩 있는가?
#
#방향키를 변수로설정하고 DFS이용...!...
#

import sys
from collections import deque
input = sys.stdin.readline
#n = input().split(' ')
n = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0]*n for _ in range(n)]
lists=[list(sys.stdin.readline()) for _ in range(n)]

apt = [] #출력값
cnt = 0 #몇단지인지 세는 변수 ㅇㅅ< 


def DFS(x,y, cnt) :
  visited[x][y] = 1 
  #global cnt 
  cnt +=1 
  for i in range(4) :
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < n :
      if lists[nx][ny] == '1' and visited[nx][ny] == 0 :
        cnt = DFS(nx, ny, cnt)

  return cnt 


for i in range(n) :
  for j in range(n) :
    if lists[i][j] == '1' and visited[i][j] == 0 :
      cnt = 0
      cnt = DFS(i, j, cnt)
      apt.append(cnt)


print(len(apt))
apt.sort()
for i in range(len(apt)):
  print(apt[i])

