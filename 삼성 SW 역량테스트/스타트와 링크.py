#백준14889 스타트와 링크
#스타트팀과 링크팀의 능력치차이 최솟값구하기
#
#
#파이썬에서 시간초과나서 함수부분 수정 => 이중포문으로 maps에 해당되는값 더하는것 수행

from sys import stdin
from copy import deepcopy
from itertools import combinations
import math

def smallsum(i, s, maps) :
    all = deepcopy(i)
    start = list(s) #스타트팀
    link = list(set(all) - set(start)) #링크팀
    start_sum = 0
    link_sum = 0
    for i in range(len(start)) :
        for j in range(len(start)) :
            if i != j :
                x,y = start[i], start[j]
                start_sum += maps[x][y]
                
                x2, y2 = link[i], link[j]
                link_sum  += maps[x2][y2]

    return abs(start_sum - link_sum)


n = int(stdin.readline())
maps = []
idx = {}
for i in range(n) :
    tmp = list(map(int, stdin.readline().split()))
    maps.append(tmp)

abc = [i for i in range(n)]
combi = list(combinations(abc, n//2))

small_sum = math.inf
for i in combi :
    #tmp = smallsum(abc, i, idx)
    tmp = smallsum(abc, i, maps)
    small_sum = min(tmp, small_sum)


print(small_sum)

===============================================================
#python3에서 시간초과발생
from sys import stdin
from copy import deepcopy
from itertools import combinations
import math

def smallsum(i, s, idx) :
    all = deepcopy(i)
    start = list(s) #스타트팀
    link = list(set(all) - set(start)) #링크팀
    start_sum = 0
    link_sum = 0

    for k,v in idx.items() :
        if k[0] in start and k[1] in start :
            start_sum += v
        if k[0] in link and k[1] in link:
            link_sum += v

    return abs(start_sum - link_sum)


n = int(stdin.readline())
maps = []
idx = {}
for i in range(n) :
    tmp = list(map(int, stdin.readline().split()))
    for t,v in enumerate(tmp) :
        if i != t :
            if (i,t) not in idx.keys() :
                if (t,i) not in idx.keys():
                    idx[(i,t)] = v
                else :
                    idx[(t,i)] += v

    maps.append(tmp)

abc = [i for i in range(n)]
combi = list(combinations(abc, n//2))

small_sum = math.inf
for i in combi :
    tmp = smallsum(abc, i, idx)
    small_sum = min(tmp, small_sum)


print(small_sum)
