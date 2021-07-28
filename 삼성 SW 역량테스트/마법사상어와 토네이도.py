
#1차시도
from copy import deepcopy
import math


n = int(input())
dxys = [[-1, 0], [0,1],[ 1,0], [0,-1]]

def moving(maps, flag, cnt ,x, y, sail) :
    maps2 = deepcopy(maps)
    calcul = []
    if flag == 0 :
        calcul = ll
    elif flag == 1 :
        calcul = dd
    elif flag == 2 :
        calcul = rr
    elif flag == 3 :
        calcul = uu

    tmp_sail = 0
    out_sail = 0
    for cx,cy, cz in calcul :
        tx,ty,tz = cx + x , cy + y, math.trunc(cz * cnt * sail)
        if 0<=tx<n and 0<=ty< n :
            maps2[tx][ty] += tz
        else :
            out_sail += tz

        tmp_sail += tz

    ax , ay = dxys[flag][0]+ x, dxys[flag][1] + y
    maps2[ax][ay] = sail - tmp_sail
    return maps2, out_sail






#x,y, %
ll =  [ [-1, -1, 0.1], [ 0,-1, 0.07], [1,-1, 0.01],
        [-1, 1, 0.1], [ 0, 1, 0.07], [1, 1, 0.01],
        [0,-2, 0.02], [0,2, 0.02], [-2,0, 0.05]]

dd = [ [-1, 1, 0.1], [-1, 0, 0.07], [-1, -1, 0.01],
       [1, 1, 0.1], [1, 0, 0.07], [1, -1, 0.01],
       [-2,0, 0.02], [2,0, 0.02], [0,2, 0.05] ]

rr  = [ [1, 1, 0.1], [1, 0, 0.07], [1, -1, 0.01],
       [-1, 1, 0.1], [-1, 0, 0.07], [-1, -1, 0.01],
       [ 0,2,  0.02], [0,-2,  0.02], [ 2,0, 0.05] ]

uu  = [ [1, -1, 0.1], [1, 0, 0.07], [1, 1, 0.01],
       [-1, -1, 0.1], [-1, 0, 0.07], [-1, 1, 0.01],
       [ 2,0,  0.02], [ -2,0,  0.02], [ 0,-2, 0.05] ]


maps = []
for i in range(n) :
    tmp = list(map(int, input().split()))
    maps.append(tmp)

print(maps)
tx, ty = n//2, n//2
out_sail = 0
flag = 0 #storm이 이동하는 방향 #1,3 일경우 배수 증가
cnt = 0 #배수증가용 변수
result = 0


while True :

    sail = maps[tx][ty]
    maps[tx][ty] = 0
    tx ,ty = dxys[flag][0] + tx, dxys[flag][1] + ty
    out_sail = 0
    maps, out_sail = moving(maps, flag, cnt, tx, ty, sail)
    result += out_sail
    if tx == 0 and ty == 0 :
        break

    if flag == 1 or flag == 3:
        cnt += 1

    flag = (flag+1) % 4

    if flag ==2 :
        break







