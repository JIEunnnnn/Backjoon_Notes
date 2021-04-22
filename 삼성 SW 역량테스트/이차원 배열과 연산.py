

#1차시도 => 오버플로우 발생.. 초기화시켜서 다시 풀어보자!
from sys import stdin
from copy import deepcopy
import math

#maps[r][c] = k가되기위한 최소시간 구하기
r,c,k = map(int, stdin.readline().split() )
maps = []


# 행계산
def rowDEF(maps, rowCnt, colCnt) :
    maps = deepcopy(maps)

    tmp_maps = [[] for _ in range(rowCnt)]
    max_cnt = 0

    for i in range(rowCnt) :
        tmp_dic = {}
        for j in range(colCnt) :

            tmp = maps[i][j]
            if tmp != 0 :
                if tmp not in tmp_dic.keys():
                    tmp_dic[tmp] = 1
                else:
                    tmp_dic[tmp] += 1

        cnt = 0
        for k, d in tmp_dic.items():
            tmp_maps[i].append((k, d))
            cnt += 1

        if max_cnt < cnt:
            max_cnt = cnt



    tmp = [[] for _ in range(rowCnt)]
    for i, m in enumerate(tmp_maps):

        m.sort(key=lambda x: (x[1], x[0]))

        if len(m) < max_cnt:
            for sz in range(max_cnt - len(m)) :
                m.append((0, 0))
        for abc in m:
            tmp[i].append(abc[0])
            tmp[i].append(abc[1])



    return tmp

#열계산..
def colDEF(maps, rowCnt, colCnt) :
    maps = deepcopy(maps)


    tmp_maps = [[] for _ in range(colCnt)]
    max_cnt = 0

    for j in range(colCnt) :
        tmp_dic = {}
        for i in range(rowCnt) :
            tmp = maps[i][j]
            if tmp != 0 :
                if tmp not in tmp_dic.keys()  :
                    tmp_dic[tmp] = 1
                else :
                    tmp_dic[tmp] +=1

        cnt = 0
        for k, d in tmp_dic.items():
            tmp_maps[j].append((k, d))
            cnt += 1

        if max_cnt < cnt:
            max_cnt = cnt



    tmp = [[] for _ in range(colCnt)]

    for i,v in enumerate(tmp_maps) :
        v.sort(key = lambda x : (x[1], x[0]))
        if len(v) < max_cnt:
            for sz in range(max_cnt - len(v)):
                v.append((0, 0))


        cnt = 0
        for abc in v :
            tmp[cnt].append(abc[0])
            tmp[cnt+1].append(abc[1])
            cnt +=2

    return tmp



for i in range(3) :
    maps.append(list(map(int, stdin.readline().split())))



for i in range(100) :

    print(r)
    print(c)

    if maps[r-1][c-1] == k :
        print(i)
        break

    if i == 99:
        print(-1)
        break


    rowCnt = len(maps)
    colCnt = len(maps[0])
    print(rowCnt)
    print(colCnt)

    if rowCnt >= colCnt :
        maps = rowDEF(maps, rowCnt, colCnt)
        print("행행행")
        print(maps)
    else :
        maps = colDEF(maps, rowCnt, colCnt)
        print("열열열")
        print(maps)

#R 연산: 배열 A의 모든 행에 대해서 정렬을 수행한다.(행의 개수 ≥ 열의 개수)
#수와 등장 횟수를 모두 넣으며, 순서는 수가 먼저이다.


#C 연산: 배열 A의 모든 열에 대해서 정렬을 수행한다. (행의 개수 < 열의 개수)


