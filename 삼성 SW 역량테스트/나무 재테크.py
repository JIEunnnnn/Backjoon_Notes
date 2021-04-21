#백준16235 나무재테크 
#K년지난후 몇개의 나무가 살아남는가?
#
#시간초과 발생해서, 블로그 참고하면서 다시 풀었다. 
#https://juhee-maeng.tistory.com/102

from sys import stdin
from copy import deepcopy
import math
from collections import defaultdict

#n*n 지도 , m개의 나무 , k년후
n,m,k = map(int, stdin.readline().split() )
dxys = [(-1,-1), (-1,0), (-1,1),  (0,-1), (0,1), (1,-1), (1,0), (1,1)]

maps = [[5 for i in range(n)]for  j in range(n)]
tree = [[{} for i in range(n)] for j in range(n)]

maps_food = []
for i in range(n):
    maps_food.append( list(map(int, stdin.readline().split())))

for i in range(m) :
    tmp = list(map(int, stdin.readline().split()))
    tree[tmp[0]-1][tmp[1]-1][tmp[2]] = 1


def BFS(maps, food , trees) :
    maps = deepcopy(maps)
    tree = deepcopy(trees)

    #봄,여름
    for i in range(n) :
        for j in range(n) :
            #if tree[i][j] != {} :
             if tree[i][j] :
                tmp_abc = {}
                die = 0
                for a in sorted(tree[i][j].keys()) :
                    if a * tree[i][j][a] <= maps[i][j] :
                        maps[i][j] -= a * tree[i][j][a]
                        tmp_abc[a+1] = tree[i][j][a]

                    else :
                        #만약 maps가 10인데, tree 가 2*6 일경우 대비
                        survive = maps[i][j] // a 
                        if not survive:  # 생존한 나무가 없음(몫이 0 일경우)
                            die += (a // 2) * tree[i][j][a]
                            continue

                        maps[i][j] -= a * survive
                        tmp_abc[a + 1] = survive

                        die += (a // 2) * (tree[i][j][a] - survive)

                tree[i][j] = tmp_abc
                maps[i][j] += die


    #가을,겨울
    for i in range(n) :
        for j in range(n) :
            maps[i][j] += food[i][j] #겨울

            if tree[i][j] :
                num = 0
                for age2 in tree[i][j].keys() :
                    if age2 % 5 == 0 :
                        num += tree[i][j][age2]
                if num :
                    for dx, dy in dxys:
                        tx, ty = i + dx, j + dy
                        if 0 <= tx < n and 0 <= ty < n:
                            if 1 not in tree[tx][ty].keys():
                                #tree[tx][ty][1] = 1
                                tree[tx][ty][1] = num
                                #num의 개수가 1개이상일 가능성도 존재하니까! 
                            else :
                                #tree[tx][ty][1] += num
                                tree[tx][ty][1] += num



    return tree, maps


# K년후 살아남은 나무의 수
for i in range(k) :
   tree, maps = BFS(maps, maps_food, tree)


cnt = 0
for i in range(n) :
    for j in range(n) :
        cnt += sum(tree[i][j].values())
print(cnt)


============================================================================
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
