#백준14891 톱니바퀴
#4개의 톱니바퀴가 극성에 따라, 어떻게 움직이는지 구하는 알고리즘
#
#deque라이브러리를 활용해서, 시간초과방지 
#방문노드추가해서 여러번 반복되는 것 방지

from sys import stdin
from copy import deepcopy
from itertools import combinations
import math
from collections import  deque


def moving(bikes, will, visited) :

    bike = deepcopy(bikes)
    num = deque([will])
    visited = deepcopy(visited)

    #2번, 6번 자리에서 극성파악하기
    while num :
        play, dir = num.popleft() # 번호와 방향(시계,반시계)
        visited[play] = 1
        play_list = deque(bike[play])

        if dir == 1 : #양옆톱니바퀴의 방향추가
            reverse_dir = -1
        else :
            reverse_dir = 1

        r, l = play_list[2], play_list[6]

        #오른쪽톱니바퀴
        r_play= play + 1
        #오버플로우 방지 및 방문X 
        if 0<= r_play < 4 and visited[r_play] != 1 :
            #같은극성이 아니면
            if bike[r_play][6] != r :
                num.append((r_play, reverse_dir ))
                
        #왼쪽톱니바퀴
        l_play = play - 1
        if 0<= l_play < 4 and visited[l_play] != 1 :
            if bike[l_play][2] != l :
                num.append((l_play,  reverse_dir ))


        if dir == 1:  # 시계방향
            tmp = play_list.pop()
            play_list.appendleft(tmp)

        else:
            tmp = play_list.popleft()
            play_list.append(tmp)

        bike[play] = play_list

    return bike


bike = deque()
for _ in range(4) :
    bike.append(list(map(int, list(stdin.readline().replace("\n","")))))

n = int(stdin.readline())
will = []
for i in range(n) :
    tmp = list(map(int, stdin.readline().split()))
    will.append((tmp[0]-1, tmp[1]))


visited = [0,0,0,0]
for i in will :
    bike = moving(bike, i, visited)

sum = 0
for i in range(4) :
    if bike[i][0] == 1 : #N=0, S=1
        sum += 2 ** i

print(sum)
