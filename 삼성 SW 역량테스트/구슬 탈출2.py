#백준13460. 구슬탈출2 
#주어진 map의 빨간구슬과 파란구슬 중 빨간구슬만 탈출시키는데 걸리는 최소한의 이동수구하기! 
#
#BFS는 최소한의 이동수 구하는데 사용되는구나 = 최단경로
#DFS는 가중치계산 및 경로제약 있을경우!!!! 

from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [list(stdin.readline()) for _ in range(n)]


for i in range(n) :
  for j in range(m) :
      if graph[i][j] == 'R':
          graph[i][j] = '.'
          red = [i, j]
      elif graph[i][j] == 'B':
          graph[i][j] = '.'
          blue = [i, j]



def move(x,y, dx, dy) :
  move =  0
  while graph[x+dx][y+dy] != '#' :
    if graph[x+dx][y+dy] == 'O' : 
      return 0,0,0
    x += dx
    y += dy 
    move += 1 

  return x,y, move 



def BFS() :
  visit = {} #방문노드 일시적 저장
  queue = deque([red + blue])
  visit[red[0], red[1], blue[0], blue[1]] = 0
 
  while queue :
    print(queue)
    print(visit) #{(3, 5, 2, 1): 5}
    

    rx, ry, bx, by = queue.popleft() #빨강, 파랑
    for dx, dy in (-1, 0), (1,0), (0, -1), (0, 1) : #상하좌우
      nrx, nry, rmove = move(rx, ry, dx, dy)
      nbx, nby, bmove = move(bx, by, dx, dy)

      if not nbx and not nby : #파랑공만 탈출할경우 = 0 
        continue 
      elif not nrx and not nry : #빨간공만 탈출하는 경우
        print(visit[rx, ry, bx, by] + 1 )
        return 

      elif nrx == nbx and nry == nby :
      # 빨간 구슬과 파란 구슬이 동시에 같은 칸에 있을 수 없다.
        if rmove >  bmove : #이동 거리가 많은 구슬을 한칸 뒤로
          nrx -= dx 
          nry -= dy 
        else :
          nbx -= dx 
          nby -= dy 
      
      if (nrx, nry, nbx, nby) not in visit :
        visit[nrx, nry, nbx, nby] = visit[rx, ry, bx, by] +1 
        queue.append([nrx, nry, nbx, nby])

    if not queue or visit[rx, ry, bx, by] >= 10 :
      print(-1)
      return 
      


print(graph)
BFS()
