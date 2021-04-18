#백준15686 치킨배달 
#치킨집과 가정집간의 거리의 합이 최솟값구하기
#
#처음에틀렸던 이유 "최대M" 을 제대로 이해X
#M보다적은수의 치킨집도 고려해야함!

from sys import stdin
from copy import deepcopy
from itertools import combinations
from collections import deque
import math

#줄, 페업하지않는 치킨집
n,m = map(int, stdin.readline().split() )

#치킨집과 가정집의 거리합이 최솟값..!
def BFS(chicken, house) :
    que = deque(chicken_permu)
    answer = math.inf #거리의 최솟값(return 용)

    while que : #폐업하지않은 치킨집중에서
        chk_chicken = que.popleft()
        mins_street = 0
        #small_mis = math.inf
        for h in house :
            small_mis = math.inf
            for i in chk_chicken:
                tmp = abs(i[0]-h[0]) + abs(i[1]-h[1])
                if small_mis > tmp :
                    small_mis = tmp #치킨집거리중 가장 작은 거리

            mins_street += small_mis

        if answer > mins_street :
            answer = mins_street



    print(answer)


chicken = []
house = []
for i in range(n) :
    tmp = list(map(int, stdin.readline().split()))
    for j in range(len(tmp)) :
        if tmp[j] == 2 :
            chicken.append((i,j))
        elif tmp[j] == 1 :
            house.append((i,j))

chicken_permu = []

#최대M중에서 M보다작은 치킨집도 허용
for j in range(1, m+1) :
    chicken_permu+= list(combinations(chicken,j ))
print(chicken_permu)
BFS(chicken_permu, house)

