#백준20055 컨베이어 벨트 위의 로봇
#주어진 k개의 0이 몇단계이후 발생하는가?
#
#문제지문이 너무 애매모호했고 그림모양이 위에서 본것X 왼쪽에서 본것.. 
#deque를 활용하여 시간초과 줄였으며, 조건에 따라 알고리즘 수행하게끔 구현

from sys import stdin
from copy import deepcopy
from itertools import combinations
import math
from collections import  deque


def moving(belt, n, k) :
    time = 0

    belt = deque(deepcopy(belt))
    robot = deque()

    while True :
        #start
        time += 1
        tmp = belt.pop()
        belt.appendleft(tmp)

        delete_robot = []
        tmp_robot = []
        if len(robot) != 0 :
            for i,v in enumerate(robot) :
                # 위의 그림에서 1번 칸이 있는 위치를 "올라가는 위치",
                # N번 칸이 있는 위치를 "내려가는 위치"라고 한다.

                # 1. 컨테이너 한번씩 이동
                will_belt = v + 1
                if will_belt < n-1 :
                    # 2. 로봇한칸 이동할때, 로봇이 존재X, 내구도 1이상
                    will_robot = will_belt + 1
                    if belt[will_robot] > 0 :
                        if will_robot not in tmp_robot :
                            belt[will_robot] -= 1
                            if will_robot < n -1 :
                                tmp_robot.append(will_robot)

                        else :
                            tmp_robot.append(will_belt)
                    else :
                        tmp_robot.append(will_belt)


        robot = tmp_robot

        if belt[0] > 0 and 0 not in robot :
            robot.append(0)
            belt[0] -=  1


        if belt.count(0) >= k :
            print(time)
            break


#2N개의 벨트, k이상의 내구성 0존재하는가

n, k = map(int, stdin.readline().split())
belt = []
belt = list(map(int, stdin.readline().split()))
moving(belt,n,k)

