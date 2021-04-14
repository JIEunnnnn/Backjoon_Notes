from sys import stdin 

#위아래오른쪽왼쪽
dx = [-1,1,0,0]
dy = [0,0,1,-1]

answer = 0 


n, m, cnt  = map(int, stdin.readline().split())
shark = {}
#maps = [[0] * m] * n 얕은복사.. 
#https://yechoi.tistory.com/52
maps = [[0 for i in range(m)] for j in range(n)] 
for i in range(cnt) :

  tmp =  list(map(int, stdin.readline().split()))
  x = tmp[0]-1
  y = tmp[1]-1
  maps[x][y] = tmp[4] 
  shark[tmp[4]] = (tmp[2], tmp[3]-1 )#크기 = 속력, 이동방향 

print(shark)


for i in range(m) : 
  
  
  for j in range(n) :
    if maps[i][j] != 0 :
        answer += maps[i][j]
        del shark[maps[i][j]]
        maps[i][j] = 0

  for j in shark :
    
