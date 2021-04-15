#백준14503 로봇청소기
#로봇청소기가 최대 몇개의 구역을 청소하는가? 
#
#처음에 구현실패원인이 방향변환과정에서 오류있었던거같다 => 제시문주의 
#BFS? 로 풀었다! 

from sys import stdin
from collections import deque

#북동남서
dxys = {0 : (0,-1,3), 1 : (-1,0, 0), 2 : (0,1, 1), 3: (1,0,2) }

#사방이벽이거나, 청소가 되어있을경우에만
dxys_others = {0 : (1,0,0), 1 : (0,-1, 1), 2 : (-1,0, 2), 3: (0,1,3)}


def bfs(start, maps) :
    howclean = 1
    q = deque()
    q.append((start[0], start[1], start[2]))
    walls = 0
    #print(q)

    while q :
        #print(q)
        #print(maps)
        x,y,z  = q.popleft()
        #좌표 (r,c) 방향 d

        for i in range(4) :
            nx, ny, z = x + dxys[z][0], y + dxys[z][1], dxys[z][2]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 0 :
                walls = 0
                howclean += 1
                q.append((nx, ny, z))
                maps[nx][ny] = 9 # 청소했음을 의미
                break

            if i == 3 :
                #한바퀴돌았는데 전부 벽 or 청소했던 경우
                ot_x, ot_y = x + dxys_others[z][0], y + dxys_others[z][1]
                q.append((ot_x, ot_y, z))
                if maps[ot_x][ot_y] == 1:
                    return howclean


    return howclean




#세로N 가로M
n,m = map(int, stdin.readline().split())
rob = list(map(int, stdin.readline().split()))
#왼쪽방향

maps = []
for i in range(n) :
    maps.append(list(map(int, stdin.readline().split())))

maps[rob[0]][rob[1]] = 9
#print(maps)
answer = bfs(rob, maps)
print(answer)
