#백준14499 주사위굴리기
#주어진지도에서 주사위굴릴때 윗면숫자출력하는 문제
#
#다양한조건을 고려해야함
#1. 지도벗어날경우 2. map에 대한 초기화 및 설정

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
direction= {1 : [0,1], 2: [0,-1] , 3 : [-1,0], 4 : [1,0]}
#초기화
now = mp[x][y]
dice[0] = now


def dice_moving(tmp) : 
  if tmp == 1 : #동
     dice[2], dice[5], dice[3], dice[0] = dice[0], dice[2], dice[5], dice[3]
  elif tmp == 2 : #서
    dice[3], dice[0], dice[2], dice[5] = dice[0], dice[2], dice[5], dice[3]

  elif tmp == 3 : #북
    dice[4], dice[5], dice[1], dice[0] = dice[0], dice[4], dice[5], dice[1] 

  elif tmp == 4 : #남
   
   dice[1], dice[0], dice[4], dice[5] = dice[0], dice[4], dice[5], dice[1]

for i in how :

  if x + direction[i][0] > n-1 or y + direction[i][1] > m-1 or x + direction[i][0] < 0 or y + direction[i][1] < 0 :
  #오버플로우발생시
  #주사위는 지도의 바깥으로 이동시킬 수 없다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다
    continue 
  else : 
    #아닐경우 
    x, y = x + direction[i][0], y + direction[i][1]
    #주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다. 
    #0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
    dice_moving(i)
    now = mp[x][y]
    
    if now != 0 :
      dice[5] = now 
      mp[x][y] = 0 
    else :
      mp[x][y] = dice[5]

    #print("테스트중")
    #print(dice)
    print(dice[0])



