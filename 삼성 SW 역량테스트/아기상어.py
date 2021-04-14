#백준16236 아기상어
#아기상어가 물고기 먹는데 걸리는 시간 구하기 
#
#조금씩.. 그래프부분이 개념 잡히는거같은데..ㅠ 
#https://dailyheumsi.tistory.com/59

#from sys import stdin 
from collections import deque 

dxs = [-1,0,0,1]
dys = [0,-1,1,0]

def bfs(x, y) :
  q, visited = deque([(x,y)]), set([(x, y)])
  time = 0
  shark = 2 
  eat = 0 
  eat_flag = False 

  answer = 0 
  while q :
    size = len(q)

    q = deque(sorted(q)) 
    #위, 왼쪽 우선순위로 물고기 냠냠

    for _ in range(size) :
      x,y = q.popleft()

      if board[x][y] != 0 and board[x][y] < shark :
        #board가 0이 아니고, shark 보다 크기가 작다면 
        board[x][y] = 0 
        eat +=1 

        if eat == shark :
          #. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.
          shark += 1 
          eat = 0
        
        #먹고나서, 위아래왼오른쪽 다시 탐색해야하므로....ㅇㅎ...
        q,visited = deque(), set([(x, y)])
        eat_flag = True 

        answer = time

      for dx, dy in zip(dxs, dys) :
        #zip = 동일한크기의 리스트의 요소를 묶어주는 함수 
        nx, ny = x + dx, y + dy 
        if nx >=0 and nx < n and ny >=0 and ny < n and (nx, ny) not in visited : 
          #오버플로우 방지 및 방문하지 않았다면 
          if board[nx][ny] <= shark :
            q.append((nx, ny))
            visited.add((nx,ny))

      if eat_flag :
        eat_flag = False 
        break 
    
    time +=1 

  return answer


n = int(input())
board = [list(map(int , input().split())) for _ in range(n)]

s_x, s_y = None, None
for i in range(n) :
    for j in range(n):
        if board[i][j] == 9:
            s_x, s_y = i, j #처음 아기상어 위치 
            board[i][j] = 0
            
# 2. 시작점에서 BFS 진행
print(bfs(s_x, s_y))
