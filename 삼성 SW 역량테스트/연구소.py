#백준14502 연구소
#바이러스가 감염되지않은 안전영역크기 최댓값 구하기
#
#
#BFS/조합/깊은복사....

from sys import stdin
from itertools import combinations
from copy import deepcopy #깊은복사는 다른 변수에 영향X
from collections import deque

dxs = [-1,1,0,0]
dys = [0,0,-1,1]

#세로크기 N 가로크기 M
n, m = map(int, stdin.readline().split())
virus =[]
empty = []
maps = []

for i in range(n) :
    maps.append(list(map(int, stdin.readline().split())))
    for j in range(m) :
        if 2 == maps[i][j] :
            virus.append((i,j)) #리스트내 튜플-> 변경X
        elif 0 == maps[i][j] :
            empty.append((i,j))

#print(maps)
#print(len(maps))
#print(len(maps[0]))

#0=빈공간, 1=벽, 2=바이러스

def count_zero(maps) :
    #print("xxxxxx")
    #print(maps)

    count = 0
    for i in range(len(maps)) :
        for j in range(len(maps[0])) :
            if maps[i][j] == 0 :
                count +=1
    return count

def bfs(start, will_walls, maps) :
    mapss = deepcopy(maps)

    for i,j in will_walls :
        mapss[i][j] = 1

    queue = deque()
    queue.extend(start)
    while queue :
        x,y = queue.popleft()
        for dx, dy in zip(dxs, dys) :
            nx, ny = x + dx, y + dy
            #print(nx, ny)
            if 0<= nx < n and 0<=ny<m and mapss[nx][ny] == 0 :
                mapss[nx][ny] = 2
                queue.append((nx,ny))

    #print(mapss)
    return count_zero(mapss)



will_walls = list(combinations(empty, 3))
#print(will_walls)

max_answer = 0
for i in will_walls :
    answer = bfs(virus, i , maps)
    if max_answer < answer :
        max_answer = answer

print(max_answer)


