#백준3190 뱀
#뱀이 사과를 만날때까지, 몇초에 게임이 끝나는가 
#
#
#https://jjangsungwon.tistory.com/27

from collections import deque


def change(d, c):
    # 상(0) 우(1) 하(2) 좌(3)
    # 동쪽 회전: 상(0) -> 우(1) -> 하(2) -> 좌(3) -> 상(0) : +1 방향
    # 왼쪽 회전: 상(0) -> 좌(3) -> 하(2) -> 우(1) -> 상(0) : -1 방향
    if c == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d


# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def start():
    direction = 1  # 초기 방향
    time = 1  # 시간
    y, x = 0, 0  # 초기 뱀 위치
    visited = deque([[y, x]])  # 방문 위치
    arr[y][x] = 2
    while True:
        y, x = y + dy[direction], x + dx[direction]
        if 0 <= y < N and 0 <= x < N and arr[y][x] != 2: 
            
            if not arr[y][x] == 1:  # 1. 사과가 없는 경우(=> 0 일경우)
                                    # 꼬리가 줄어들며, 몸길이의 변화가 없다 
                temp_y, temp_x = visited.popleft()
                arr[temp_y][temp_x] = 0  # 꼬리 제거
                
            arr[y][x] = 2     # 2. 사과가 있는 경우
                              # 지나간 자리는 2로 수정하기
            visited.append([y, x])
            if time in times.keys(): #방향 바꾸는것 존재하는 경우
                direction = change(direction, times[time])
            time += 1
        else:  # 본인 몸에 부딪히거나, 벽에 부딪힌 경우
            return time


if __name__ == "__main__":

    # input
    N = int(input())
    K = int(input())
    arr = [[0] * N for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        arr[a - 1][b - 1] = 1  # 사과 저장
    L = int(input())
    times = {}
    for i in range(L):
        X, C = input().split()
        times[int(X)] = C
    print(start())

===============================================================
#1차시도
from sys import stdin


size =  int(stdin.readline()) #보드의 크기
apple = int(stdin.readline()) #사과 갯수
apple_direc = []
for i in range(apple) :
  apple_direc.append(list(map(int,stdin.readline().split())))
dummy = int(stdin.readline()) #뱀의방향전환횟수?
dummy_list = []
for i in range(dummy) :
  dummy_list.append(list(stdin.readline().split()))

print(apple_direc)
print(dummy_list)
#n = list(map(int, stdin.readline().split())) #숫자
#num = list(map(int, stdin.readline().split())) #연산자 갯수
