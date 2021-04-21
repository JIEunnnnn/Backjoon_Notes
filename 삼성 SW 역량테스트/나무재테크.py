

#1차시도 => 시간초과
from sys import stdin
from copy import deepcopy
from itertools import combinations
from collections import deque
import math

#n*n 지도 , m개의 나무 , k년후
n,m,k = map(int, stdin.readline().split() )
dxys = [(-1,-1), (-1,0), (-1,1),  (0,-1), (0,1), (1,-1), (1,0), (1,1)]
max_sum = 0

def BFS(maps, food , trees) :
    maps = deepcopy(maps)
    tree = deepcopy(trees)
    deadtree = deque()

    # 봄 : 나이어린순부터 양분섭취하며 +1, 나이만큼 먹지못하면 죽음
    cnt = 0 #tree오버플로우방지
    for idxs ,i in enumerate(trees) :
        x,y = i[0], i[1]
        idx = idxs - cnt
        if maps[x][y] < i[2] :
            tree.pop(idx)
            cnt += 1

            deadtree.append((x,y,i[2]))
        else :
            maps[x][y] -= i[2]
            tree[idx][2] +=1

    # 여름 : 봄에죽은나무가 양분이 됨, 죽은나무 나이의 2로나눈값이 양분(소수점아래는 버림)
    if len(deadtree) != 0 :
        for i in deadtree  :
            x,y = i[0], i[1]
            maps[x][y] +=  math.floor(i[2]/2)



    # 가을 : 나무 번식(5의배수의 나무들만)
    #               인접한 8개의 칸에 나이가 1인나무 생겨남(땅벗어나면 나무X)
    for i in tree :
        if i[2]%5 == 0 :

            for dx,dy in dxys :
                tx , ty = i[0]+dx, i[1] +dy
                if 0<=tx<n and 0<=ty<n :
                    tree.append([tx,ty,1])


    # 겨울 : 땅에 양분추가 A[r][c]
    for i,v in enumerate(maps) :
        for j,v2 in enumerate(v) :
            maps[i][j] += food[i][j]

    return tree, maps



maps = [[5 for i in range(n)]for  j in range(n)]

maps_food = []
for i in range(n):

    maps_food.append( list(map(int, stdin.readline().split())))


tree = []
for i in range(m) :
    tmp =list(map(int, stdin.readline().split()))
    tmp[0], tmp[1] = tmp[0]-1, tmp[1]-1
    tree.append(tmp)


# K년후 살아남은 나무의 수
for i in range(k) :
    tree.sort(key = lambda x: x[2])
    tree, maps = BFS(maps, maps_food, tree)

print(len(tree))
