#백준15685 드래곤 커브 
#몇개의 드래곤커브가 있는가? 
#
#결국, 드래곤커브의 규칙 및 오버플로우 등을 생각해야했다
#몇개월만에 푸니까 너무 어려웠어...ㅠ

n = int(input())

graph = [[0] * 101 for _ in range(101)]
dx = [0,-1,0,1]
dy = [1,0,-1,0]
    # 0 = x좌표 증가, 1 = y좌표 감소, 2 = x좌표감소, 3 = y좌표 증가

for i in range(n) :

    y,x,d,g = map(int, input().split(' '))
    graph[x][y] =1

    #커브리스트 만들기
    curve = [d]
    for j in range(g) : #g= 드래곤커브 세대(3세대일경우,  3번반복문 - curve리스트)
        for k in range(len(curve) -1, -1, -1) : #start, stop, step(역순)

            curve.append((curve[k]+1) % 4)

    for j in range(len(curve)) :
        x += dx[curve[j]]
        y += dy[curve[j]]

        if x <0 or x >= 101 or y <0 or y >= 101 :
            continue

        graph[x][y] = 1

    #print(curve)

answer = 0

for i in range(100) : #오버플로우방지
    for j in range(100) :
        if graph[i][j] == 1 and graph[i+1][j] == 1 and graph[i][j+1] == 1 and graph[i+1][j+1] == 1 :
            #드래곤커브는 4개의 꼭지점이 존재할 때
            answer +=1

print(answer)





