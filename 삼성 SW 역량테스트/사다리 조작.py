#백준15684 사다리 조작
#최대 3개의 사다리 조작해서, i번째에 i 가 출력되는 사다리 게임
#
#1차시도 때, 가로-세로 로 구현했는데 이게 많이 헷갈렸다. + 조합X dfs로 풀기!
#다른 풀이 참고하니까 maps[세로][가로]로 구현함(유동적으로 풀자!)
#https://chldkato.tistory.com/151

import sys

input = sys.stdin.readline
n,m,h = map(int, input().split()) #세로, 연결할 가로수, 가로
maps = [[0]*h for _ in range(n)] #maps[세로][가로]

def move() :
    #검사하는 메소드
    for i in range(n) :
        num = i
        for j in range(h) :
            if maps[num][j] :
                num +=1
            elif maps[num-1][j] :
                num -= 1
        if i != num :
            return 0
    return 1

#어느 가로선을 연결할 것인가?
def dfs(cnt, idx, r) :
    #print(maps)
    global ans
    if cnt == r :
        if move() == 1 :
            ans = cnt
        return
    
    for i in range(idx, h) : #가로 - 추가해야할 가로선(idx 이후만 검사하기)
        for j in range(n-1) : #세로선(마지막 세로선 제외-5개의 세로선이라면 4번째 세로선 영향받으니까... )
            if maps[j][i] : #maps[j][i] = 1 일경우
                continue
            if j-1 >= 0 and maps[j-1][i]:
                continue
            if j + 1 < n and maps[j + 1][i]:
                continue

            maps[j][i] = 1
            dfs(cnt + 1, i, r)
            maps[j][i] = 0



for _ in range(m) :
    x, y = map(int, input().split()) #가로선, 세로선
    maps[y-1][x-1] = 1 #연결관계 저장

#print(maps)
ans, flag =sys.maxsize, 1
for r in range(4) :
    dfs(0,0,r) #최대3개의 가로선추가,,,
    if ans != sys.maxsize:
        print(ans)
        flag = 0
        break

if flag == 1 :
    print(-1)

======================================================================
#1차시도.. => 테케도 통과못함ㅠ 뭐가문제지.. 
from sys import stdin
from copy import deepcopy
from itertools import combinations

dxs = [(0,1),(0,-1)]
n,m,h = map(int, stdin.readline().split())
#세로선,  가로선추가, 가로선

# 단, 두 가로선이 연속하거나 서로 접하면 안 된다. 또, 가로선은 점선 위에 있어야 한다.
#i번 사다리는 i번나와야함
def line_append(maps, will_lines) :
    maps = deepcopy(maps)
    flag = 0

    for w in will_lines :
        x, y, x2, y2 = w[0], w[1], w[2], w[3]
        maps[x][y] = 1
        maps[x2][y2] = 1

    cnt = 0

    for y in range(n) :
        tmp = y
        for x in range(h) :
            if maps[x][tmp] == 1 :
                for dx, dy in dxs :
                    tx, ty = x + dx, tmp + dy
                    if 0<= tx < h and 0 <= ty < n :
                        if maps[tx][ty] == 1 :
                            tmp = ty
                            break

        if tmp == y:
            cnt +=1


    if cnt == n :
        print("tlqkf")
        return True
    else :
        return False


lines = []
maps = [[0 for i in range(n)] for j in range(h)]
will_lines = []

# 세로선, 가로선
#(1 ≤ a ≤ H, 1 ≤ b ≤ N-1)
# b, b+1 세로선 을 a점선에서 연결하기
for _ in range(m) :
    tmp = list(map(int, stdin.readline().split()))
    maps[tmp[0]-1][tmp[1]-1] = 1
    maps[tmp[0]-1][tmp[1]] = 1
    # (1 ≤ a ≤ H, 1 ≤ b ≤ N-1)
for x in range(h) :
    for y in range(n) :
        if maps[x][y] == 0 :
            tx, ty = x , y + 1
            if 0<=tx< h and 0<=ty < n :
                if maps[tx][ty] == 0 :
                    will_lines.append((x, y, tx, ty ))

print(will_lines)
print(maps)
for i in range(1, 4) :
    #tmp = list(combinations(will_lines, i))
    tmp = list(combinations(will_lines, 3))
    for j in tmp :
        ans = line_append(maps, j)
        if ans == False :
            continue
        else :
            print("정답!!!!!!!")
            print(i)
            break
