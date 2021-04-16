

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
