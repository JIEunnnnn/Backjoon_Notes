from sys import stdin 

#지도크기, 좌표위치, 명령개수
n,m,x,y,num =  map(int, stdin.readline().split())

#지도
mp = [[]] * n

for i in range(n) :
  mp[i] = list(map(int, stdin.readline().split()))

#명령어순서
how = list(map(int, stdin.readline().split()))

dice = [0,0,0,0,0,0]
direction= {1 : [1,0], 2: [-1, 0] , 3 : [0,-1], 4 : [0,1]}
#초기화
now = mp[x][y]
dice[0] = now

for i in how :
  tmp = direction[i]
  #오버플로우발생시

  #아닐경우 
  now = mp[x+tmp[0]][y+tmp[1]]
