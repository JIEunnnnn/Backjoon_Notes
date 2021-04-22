#백준17140 이차원 배열과 연산
#행과열의 길이에 따라 계산다르게 수행하는 알고리즘
#
#1차시도때, 의도는 좋았으나,row, col변환해야하는 과정에서 오버플로우 발생! 
#파이썬에서 zip(*A) 를 활용하여, 행과열을 바꾸는 "전치행렬" 구현이 가능하다 => 튜플로 반환되니까 list(maps(list, zip(*A))) 로! 
#또한 Counter메소드를 활용하여, 딕셔너리형태의 갯수를 구할수있다는 점...! 

# https://inspirit941.tistory.com/166 (참고블로그)
# http://pyengine.blogspot.com/2016/11/python-zip-transpose.html (전치행렬)


from sys import stdin
from collections import Counter
from copy import deepcopy

r,c,k = map(int, stdin.readline().split())
maps = []

for i in range(3) :
    maps.append(list(map(int, stdin.readline().split())))

#행계산
def rowDEF(maps) :
    maps = deepcopy(maps)
    max_col = 0    #최대길이에 맞춰 0을 추가해야함
    next_maps = [] #리턴할 maps

    for rows in maps :
        next_row = []
        tmp = Counter(rows)
        tmp2 =  list(tmp.items())
        tmp2.sort(key = lambda x : (x[1], x[0]))
        for num, cnt in tmp2 :
            if num != 0 :
                next_row.append(num)
                next_row.append(cnt)
        max_col =  max(max_col, len(next_row))
        next_maps.append(next_row)

    for rows in next_maps :
        if len(rows) < max_col :
            for i in range(max_col - len(rows)) :
                rows.append(0)

    return next_maps




for i in range(101) :
    if r <= len(maps) and c <= len(maps[0]) and maps[r-1][c-1] == k :
        #오버플로우 방지
        print(i)
        break
    if i == 100 :
        print(-1)

    if len(maps) >= len(maps[0]) :
        maps = rowDEF(maps)
    else :
        #전치행렬, 행과열을 바꾸는 연산방법!
        # 1) 열을 행으로 변환하여 계산시행

        #print(maps)
            # [[2, 1, 1, 2, 0, 0], [1, 1, 2, 1, 3, 1], [3, 3, 0, 0, 0, 0]]
        maps2 = list(zip(*maps))
            #[(2, 1, 3), (1, 1, 3), (1, 2, 0), (2, 1, 0), (0, 3, 0), (0, 1, 0)]
        maps3 = list(map(list, maps2))
            #[[2, 1, 3], [1, 1, 3], [1, 2, 0], [2, 1, 0], [0, 3, 0], [0, 1, 0]]

        maps = rowDEF(maps3)

        # 2) 행으로 변환했던 열을 다시 열로 변환해야함!
        maps = list(map(list, zip(*maps)))



========================================================================
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


