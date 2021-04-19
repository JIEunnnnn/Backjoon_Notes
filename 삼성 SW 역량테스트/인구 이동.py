

#2차시도 ==> 시간초과,,,,
from sys import stdin
from copy import deepcopy
from itertools import combinations
from collections import deque
import math


#N*N의 맵, l <= 두나라의 인구차이(국경선열리는조건) <= r
n,l,r = map(int, stdin.readline().split() )
maps = []
dxs = [-1,1,0,0]
dys = [0,0,-1, 1]
for i in range(n):
    maps.append(list(map(int, stdin.readline().split())))


def visited(maps, i, j) :
    x, y, sum = i, j, 0
    start = deque([(x,y)])
    visited = [] #return 값(maps변경위한..!)

    while start :
        vx, vy = start.popleft()
        for dx,dy in zip(dxs, dys) :
            tx, ty = vx + dx, vy+ dy
            if 0 <=tx < n and 0 <= ty  < n :
                if l <= abs(maps[vx][vy] - maps[tx][ty]) <= r :
                    if (vx,vy) not in visited :
                        visited.append((vx,vy))
                        sum += maps[vx][vy]

                    if (tx,ty) not in visited :
                        visited.append((tx,ty))
                        sum += maps[tx][ty]
                        start.append((tx,ty))


    return visited, sum

def BFS(maps, cnt):
    tmaps = deepcopy(maps)
    total_visited = []
    total = set()
    sum = 0
    flag = 0

    for i in range(n) :
        for j in range(n) :
            if (i,j) not in total :
                total_visited, sum = visited(maps, i, j)
                total.update(total_visited)

                if len(total_visited) != 0 :
                    flag = 1
                    abc = math.floor(sum / len(total_visited))
                    for x,y in total_visited :
                        tmaps[x][y] = abc


    #하루지나는것이 인구이동의미...                     
    if flag == 1 :
        cnt += 1

    return tmaps, cnt, flag


cnt = 0

while True :
    maps, cnt, flag = BFS(maps, cnt)
    if flag == 1 :
        continue
    else :
        print(cnt)
        break

==========================================================================
#1차시도 실패 => 연합이 2개이상일경우 고려X
from sys import stdin
from copy import deepcopy
from itertools import combinations
from collections import deque
import math


#N*N의 맵, l <= 두나라의 인구차이(국경선열리는조건) <= r
n,l,r = map(int, stdin.readline().split() )
maps = []
dxs = [-1,1,0,0]
dys = [0,0,-1,1]
for i in range(n):
    maps.append(list(map(int, stdin.readline().split())))

print(maps)


def BFS(maps, cnt):
    tmap = deepcopy(maps)
    insert_xy = deque()
    sum = 0
    for i,i_value in enumerate(maps):
        #print(i)
        for j, j_value in enumerate(i_value):
            for idx, (dx, dy) in enumerate(zip(dxs, dys)):
                flag = 0
                tx, ty = i + dx, j + dy
                if 0 <= tx < n and 0 <= ty < n:  # 오버플로우방지

                    if l <= abs(maps[i][j] - maps[tx][ty]) <= r and (i, j) not in insert_xy:
                        insert_xy.append((i, j))
                        sum += maps[i][j]
                        flag = 1

                        break

    if len(insert_xy) == 0 :
        print(cnt)
    else :
        cnt += 1
        abc = math.floor(sum/len(insert_xy))
        for i,j in insert_xy :
            tmap[i][j] = abc
        print(tmap)
        print(insert_xy)
        BFS(tmap, cnt)



BFS(maps, 0 )
