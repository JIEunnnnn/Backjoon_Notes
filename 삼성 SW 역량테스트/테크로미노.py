#백준14500 테크로미노
#주어진모형5개의 위치에 따른 요소들의 최댓값구하기 
#
#테크로미노 리스트로 위치 저장하여 for문돌리기
#처음 테크로미노 정의시 혯갈... 그려서 확인해보자! 

from sys import stdin
from copy import deepcopy
from itertools import combinations
from collections import deque
import math

#n*m 지도
n,m = map(int, stdin.readline().split() )
dxs = [-1,1,0,0]
dys = [0,0,-1,1]
max_sum = 0

techromino = [
    [(0,0),(0,1),(0,2),(0,3)], #첫번째모형 - 
    [(0,0),(1,0),(2,0),(3,0)],
    [(0,0),(0,1),(1,0),(1,1)], #두번째모형 ㅁ
    [(0,0),(1,0),(2,0),(2,1)], #세번째모형 ㄴ
    [(0,0),(0,1),(0,2),(1,0)],
    [(0,0),(0,1),(1,1),(2,1)],
    [(0,2),(1,0),(1,1),(1,2)],
    [(0,1),(1,1),(2,1),(2,0)], #세번째모형반전
    [(0,0),(1,0),(1,1),(1,2)],
    [(0,0),(1,0),(2,0),(0,1)],
    [(0,0),(0,1),(0,2),(1,2)],
    [(0,0),(1,0),(1,1),(2,1)], #네번째모형 번개
    [(1,0),(1,1),(0,1),(0,2)],
    [(0,1),(1,0),(1,1),(2,0)], #네번째모형반전
    [(0,0),(0,1),(1,1),(1,2)],
    [(0,0),(0,1),(0,2),(1,1)], #다섯번째모형 ㅜ 
    [(1,0),(0,1),(1,1),(2,1)],
    [(0,1),(1,0),(1,1),(1,2)],
    [(0,0),(1,0),(2,0),(1,1)]
]


def BFS(maps, tech) :
    max_tmp = 0
    for i in range(n) :
        for j in range(m) :
            tmp = 0
            for t in tech :
                #print(t)
                tx, ty = i + t[0], j + t[1]
                if 0<=tx < n and 0 <= ty < m :
                    tmp += maps[tx][ty]
                else :
                    tmp = 0
                    break

            if max_tmp < tmp :
                max_tmp = tmp


    #print(max_tmp)
    return max_tmp



maps = []
for i in range(n):
    tmp = list(map(int, stdin.readline().split()))
    maps.append(tmp)

for t in techromino :
    #answer = BFS(maps, t)
    answer = BFS(maps, t)
    if max_sum < answer :
        max_sum = answer

print(max_sum)


