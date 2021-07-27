#백준20056 마법사 상어와 파이어볼 
#마법사 상어가 k가 이동한후, 남아있는 파이어볼 질량의 합은?
#
#
#문제이해하기 급급했다ㅠ + 예외처리하는 것 잊지말자 

from copy import deepcopy

n, m, k = map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]

for i in range(m) :
    r,c,m,s,d = map(int, input().split())
    if m != 0 : #질량이 0이 아니면
        print(r)
        print(c)
        board[r-1][c-1].append([m,s,d])
        print(board)
        print()

# r[y][x]
dirs = [[-1,0] , [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1]]
#print(board)
#print()

for i in range(k) :
    n_board = [[[] for _ in range(n)] for _ in range(n)]

    #모든 파이어볼을 이동시킨다.
    for y in range(n):
        for x in range(n):
            if board[y][x] != [] :
                for b in range(len(board[y][x])) :
                    tmp_m, tmp_s, tmp_d = board[y][x][b] #질량, 속도, 방향
                    tmp_y, tmp_x = y + dirs[tmp_d][0] * tmp_s , x + dirs[tmp_d][1] * tmp_s
                    tmp_y = (tmp_y + n) % n
                    tmp_x = (tmp_x + n) % n

                    n_board[tmp_y][tmp_x].append([tmp_m, tmp_s, tmp_d])


    #2개이상의 파이어볼이 있을 경우

    #m=질량, d=방향, s=속력
    for y2 in range(n):
        for x2 in range(n) :
            if len(n_board[y2][x2]) > 1 :
                m2, s2, d2 = 0, 0, []
                cnt = len(n_board[y2][x2])
                for c in range(cnt) :
                    m2 += n_board[y2][x2][c][0] #질량
                    s2 += n_board[y2][x2][c][1] #속도
                    d2.append(n_board[y2][x2][c][2] % 2 ) #방향
                    #짝수일경우 = 0 홀수일경우 = 1

                m2 = int(m2 / 5)
                s2 = int(s2 / cnt)
                n_board[y2][x2] = []
                if m2 != 0 :
                    if sum(d2) == 0 or sum(d2) == cnt :
                        #모두 짝수일경우 == 0 , 모두 홀수일경우 == len(n_board[y2][x2])
                        for i in range(4) :
                            n_board[y2][x2].append([m2,s2, i * 2])
                    else :
                        for j in range(4) :
                            n_board[y2][x2].append([m2,s2, j * 2 + 1])

    #print(n_board)
    #print()
    board = deepcopy(n_board)

# 남아있는 파이어볼 질량의 합 구하기
sum_m = 0
for y in range(n):
    for x in range(n):
        if board[y][x] != []:
            for b in range(len(board[y][x])):
                sum_m += board[y][x][b][0] #질량더하기
print(sum_m)
