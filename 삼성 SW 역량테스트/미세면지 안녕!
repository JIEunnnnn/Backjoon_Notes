#백준17144 미세먼지 안녕!
#주어진 T초동안 미세먼지이동 및 공기청정기 작동하여 남은 미세먼지 양은?  
#
#공기청정기 위, 아래로 분리하여 알고리즘 구현 및 BFS로 구현??
#pypy3는 맞았지만 python3 는 시간초과 발생..!

from sys import stdin
from copy import deepcopy
from collections import deque
import math

#r*c 지도, t초
r,c,t = map(int, stdin.readline().split() )
dxs = [-1,1,0,0]
dys = [0,0,-1,1]

def BFS_air_UP(maps, air) :
    maps =deepcopy(maps)
    x,y = air # (2,0)
    tx, ty = 0, 0
    tmp, maps[x][y + 1] = maps[x][y + 1], 0
    tmp2 = 0

    #RIGHT
    for i in range(2, c) :
        tx, ty = x, i
        tmp2 = maps[tx][ty]
        maps[tx][ty] = tmp
        tmp = tmp2

    for i in range(x-1,-1,-1) :
        tx, ty = i, ty
        tmp2 = maps[tx][ty]
        maps[tx][ty] = tmp
        tmp = tmp2

    for i in range(c-2, -1, -1) :
        tx, ty = tx , i
        tmp2 = maps[tx][ty]
        maps[tx][ty] = tmp
        tmp = tmp2

    for i in range(1, x) :
        tx,ty = i, ty
        tmp2 = maps[tx][ty]
        maps[tx][ty] = tmp
        tmp = tmp2

    return maps

def BFS_air_DOWN(maps, air) :
    maps = deepcopy(maps)
    x, y = air  # (3,0)
    tx, ty = 0, 0
    tmp, maps[x][y + 1] = maps[x][y + 1], 0
    tmp2 = 0

    # RIGHT
    for i in range(2, c):
        tx, ty = x, i
        tmp2 = maps[tx][ty]
        maps[tx][ty] = tmp
        tmp = tmp2


    for i in range(x+1, r):
        tx, ty = i, ty
        tmp2 = maps[tx][ty]
        maps[tx][ty] = tmp
        tmp = tmp2


    for i in range(c - 2, -1, -1):
        tx, ty = tx, i
        tmp2 = maps[tx][ty]
        maps[tx][ty] = tmp
        tmp = tmp2

    for i in range(tx - 1, x, -1):
        tx, ty = i, ty
        tmp2 = maps[tx][ty]
        maps[tx][ty] = tmp
        tmp = tmp2

    return maps



def BFS(maps, tmaps, dust) :
    tmaps = deepcopy(tmaps)

    while dust :
        x,y = dust.popleft()
        tmp = math.floor(maps[x][y] / 5)
        cnt = 0
        for dx, dy in zip(dxs, dys) :
            tx, ty = x + dx, y + dy
            if 0 <= tx < r and 0<= ty < c and maps[tx][ty] != -1 :
                tmaps[tx][ty] += tmp
                cnt +=1

        tmaps[x][y] = tmaps[x][y] + (maps[x][y] -  (tmp * cnt))

    return tmaps




maps = []
tmaps = [[0 for i in range(c)] for j in range(r)]
dust = deque()
air = deque()
for i in range(r):
    tmp = list(map(int, stdin.readline().split()))
    maps.append(tmp)
    for j,v in enumerate(tmp) :
        if v == -1 : #공기청정기 위치 -1
            tmaps[i][j] = -1
            air.append((i,j))
        elif v != 0 :
            dust.append((i,j))


for i in range(t) :
    maps = BFS(maps, tmaps, dust)
    maps = BFS_air_UP(maps, air[0])
    maps = BFS_air_DOWN(maps, air[1])

    dust = deque([])
    for i,v in enumerate(maps) :
        for j, k in enumerate(v) :
            if k != 0 and k != -1 :
                dust.append((i,j))




sum = 2
for i in maps :
    for j in i :
        sum += j

print(sum)


