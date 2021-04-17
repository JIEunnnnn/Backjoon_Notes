#백준15683 감시
#감시카메라의 사각지대 최솟값 구하기
#
#DFS 구현(재귀)
#https://inspirit941.tistory.com/165
#
#for => DFS => return 마지막카메라까지 접근할경우 
#다시for문시행해서 방향수정


from sys import stdin
from collections import deque
from copy import deepcopy
import math

#cctv = {1:(0,1), 2:(0,-1), 3 : (-1,0), 5: (1,0) }
dxs = [0,0,-1,1]
dys = [1,-1,0,0]

#세로N 가로M
n,m = map(int, stdin.readline().split())
answer = math.inf

def change(maps, list, x, y) :
    maps = deepcopy(maps)

    for i in list :
        if i == 0 : #오른쪽
            for i in range(y , m) :
                if maps[x][i] == 6 :
                    break
                elif maps[x][i] != 0 :
                    continue
                else :
                    maps[x][i] = '#'

        elif i == 1 : #왼쪽
            for i in range(y,-1,-1) :
                if maps[x][i] == 6:
                    break
                elif maps[x][i] != 0:
                    continue
                else:
                    maps[x][i] = '#'

        elif i == 2 : #위쪽
            for i in range(x,-1,-1) :
                if maps[i][y] == 6 :
                    break
                elif maps[i][y] != 0 :
                    continue
                else :
                    maps[i][y] = '#'

        elif i == 3 : #아래쪽

            for i in range(x,n) :
                if maps[i][y] == 6 :
                    break
                elif maps[i][y] != 0 :
                    continue
                else :
                    maps[i][y] = '#'

    return maps


def DFS(cctvs, maps, idx) :
    global answer
    
    #마지막감시카메라 시행할때까지 재귀반복
    if idx == len(cctvs) :
        value = 0
        for i in range(len(maps)) :
            value += maps[i].count(0)

        answer = min(answer, value)
        return

    cctv = cctvs[idx]
    num, x,y = cctv[0], cctv[1], cctv[2]

    if num == 1 :
        for i in range(4) :
            next_maps = change(maps, [i], x,y )
            DFS(cctvs, next_maps, idx+1)

    elif num == 2 :
        for i in [(0,1), (2,3)] :
            next_maps = change(maps, i, x,y )
            DFS(cctvs, next_maps, idx+1)


    elif num == 3 :
        for i in [(0,2), (3,0), (1,3), (2,1)] :
            next_maps = change(maps, i, x,y )
            DFS(cctvs, next_maps, idx+1)

    elif num == 4 :
        for i in [(0,2,1), (3,0,2), (1,3,0), (2,1,3)] :
            next_maps = change(maps, i, x,y )
            DFS(cctvs, next_maps, idx+1)

    elif num == 5 :
        i = (0,1,2,3)
        next_maps = change(maps, i, x, y)
        DFS(cctvs, next_maps, idx + 1)


cctv = []
maps = []
for i in range(n) :
    tmp = list(map(int, stdin.readline().split()))
    for key, value in enumerate(tmp) :
        if value in [1,2,3,4,5] :
            cctv.append((value, i, key))

    maps.append(deepcopy(tmp))



#print(cctv)
#print(maps)
DFS(cctv, maps, 0 )
#print(maps)
print(answer)
==================================================================
#1차시도 실패>_<77
from sys import stdin
from collections import deque
from copy import deepcopy

#cctv = {1:(0,1), 2:(0,-1), 3 : (-1,0), 5: (1,0) }
dxs = [0,0,-1,1]
dys = [1,-1,0,0]

#세로N 가로M
n,m = map(int, stdin.readline().split())

def direction(x, i) :
    list = []
    if x == 1:
        list.append((dxs[i],dys[i]))

    elif x == 2 :
        if i % 2 == 0 :
            list.append((dxs[0], dys[0]))
            list.append((dxs[1], dys[1]))
        else :
            list.append((dxs[2], dys[2]))
            list.append((dxs[3], dys[3]))

    elif x == 3 :
        if i == 0:
            list.append((-1, 0))
        elif i == 1:
            list.append((0, 1))
        elif i == 2:
            list.append((1, 0))
        elif i == 3:
            list.append((0, -1))

        list.append((dxs[i],dys[i]))

    elif x == 4 :

        if i == 0:
            list.append((-1, 0))
        elif i == 1:
            list.append((0, 1))
        elif i == 2:
            list.append((1, 0))
        elif i == 3:
            list.append((0, -1))

        if i % 2 == 0 :
            list.append((dxs[0], dys[0])) #(0,1)
            list.append((dxs[1], dys[1])) #(0,-1)
        else :
            list.append((dxs[2], dys[2]))
            list.append((dxs[3], dys[3]))

    #5번은 1번만돌리면되고
    elif x == 5 :
        list.append((dxs[0], dys[0]))
        list.append((dxs[1], dys[1]))
        list.append((dxs[2], dys[2]))
        list.append((dxs[3], dys[3]))

    return list

def BFS(cctv, maps) :
    que = deque(cctv)
    #print(que)
    while que :
        answer = 0
        tmp = que.popleft()
        maxchange = []
        for i in range(4) :
            list = direction(tmp[0], i)
            willchange = []
            for dx, dy in list:
                x, y = tmp[1], tmp[2]
                while True:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if maps[nx][ny] == 0:
                            willchange.append((nx, ny))
                            x, y = nx, ny
                        elif maps[nx][ny] == 6:
                            break
                        else:
                            x, y = nx, ny
                            continue
                    else:
                        break

                if len(maxchange) < len(willchange):
                    maxchange = willchange


        #print("맥스부분임")
        #print(maxchange)
        for x,y in maxchange :
            maps[x][y] = '#'

cctv = []
maps = []
for i in range(n) :
    tmp = list(map(int, stdin.readline().split()))
    for key, value in enumerate(tmp) :
        if value in [1,2,3,4,5] :
            cctv.append((value, i, key))

    maps.append(tmp)



#print(cctv)
#print(maps)
BFS(cctv,maps)
print(maps)
answer = 0
for x in maps :
    for j in x :
        if j == 0 :
            answer += 1

print(answer)
