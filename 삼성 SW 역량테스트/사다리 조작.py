



#1차시도.. => 테케도 통과못함ㅠ 뭐가문제지.. 
from sys import stdin
from copy import deepcopy
from itertools import combinations
import math
from collections import  deque

dxs = [(0,1),(0,-1)]
n,m,h = map(int, stdin.readline().split())
#세로선,  가로선추가, 가로선

# 단, 두 가로선이 연속하거나 서로 접하면 안 된다. 또, 가로선은 점선 위에 있어야 한다.
#i번 사다리는 i번나와야함
def line_append(maps, will_lines) :
    maps = deepcopy(maps)
    flag = 0

    for w in will_lines :
        x, y, x2, y2 = w[0], w[1], w[2], w[3]
        maps[x][y] = 1
        maps[x2][y2] = 1

    cnt = 0

    for y in range(n) :
        tmp = y
        for x in range(h) :
            if maps[x][tmp] == 1 :
                for dx, dy in dxs :
                    tx, ty = x + dx, tmp + dy
                    if 0<= tx < h and 0 <= ty < n :
                        if maps[tx][ty] == 1 :
                            tmp = ty
                            break

        if tmp == y:
            cnt +=1


    if cnt == n :
        print("tlqkf")
        return True
    else :
        return False


lines = []
maps = [[0 for i in range(n)] for j in range(h)]
will_lines = []

# 세로선, 가로선
#(1 ≤ a ≤ H, 1 ≤ b ≤ N-1)
# b, b+1 세로선 을 a점선에서 연결하기
for _ in range(m) :
    tmp = list(map(int, stdin.readline().split()))
    maps[tmp[0]-1][tmp[1]-1] = 1
    maps[tmp[0]-1][tmp[1]] = 1
    # (1 ≤ a ≤ H, 1 ≤ b ≤ N-1)
for x in range(h) :
    for y in range(n) :
        if maps[x][y] == 0 :
            tx, ty = x , y + 1
            if 0<=tx< h and 0<=ty < n :
                if maps[tx][ty] == 0 :
                    will_lines.append((x, y, tx, ty ))

print(will_lines)
print(maps)
for i in range(1, 4) :
    #tmp = list(combinations(will_lines, i))
    tmp = list(combinations(will_lines, 3))
    for j in tmp :
        ans = line_append(maps, j)
        if ans == False :
            continue
        else :
            print("정답!!!!!!!")
            print(i)
            break
