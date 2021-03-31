#백준12100 2048(Easy)
#주어진 입력값에 따라 상하좌우값 더해서 최대값 구하는 알고리즘 
#
#조금만 복잡하면 생각안하는 습관을 고치자..! (쫌만 생각하면 풀수있는 문제였을텐데..)
#https://juhee-maeng.tistory.com/90

import copy 

def find_max(array) :
  global maxv 
  for i in range(N):
    for j in range(N):
      if maxv < array[i][j] :
        maxv = array[i][j]

def move_left(board) :
  for i in range(N) :
    p = 0
    x = 0
    for q in range(N) :
     
      if board[i][q] == 0 : #0이면 건너뛰기
        continue 
      if x == 0 :
        x = board[i][q]
      else :
        if x == board[i][q] :
          board[i][p] = 2 * x
          p = p+1 
          x = 0
        else :
          # q가 1이라면 p 는 0번째 자리 
          board[i][p] = x 
          p = p + 1 
          x = board[i][q] 

      board[i][q] = 0 #블록이동했으므로 0으로 초기화

    if x != 0 :
      board[i][p] = x 
  #print(board)
  return board

def move_right(board) :
  for i in range(N) :
    p = N -1 
    x = 0
    for q in range(N-1, -1, -1):
      if board[i][q] == 0 :
        continue 
      if x == 0 :
        x = board[i][q] 
      else :
        if x == board[i][q] :
          board[i][p] = 2 * x
          p = p-1 
          x = 0
        else :
          board[i][p] = x 
          p = p - 1 
          x = board[i][q] 
      
      board[i][q] = 0 

    if x != 0 :
        board[i][p] = x 
  print(board)
  return board

def move_up(board) :
  for i in range(N) :
      p = 0
      x = 0
      for q in range(N) :
        if board[q][i] == 0:
          continue 
        if x == 0 :
          x = board[q][i]
        else :
          if x == board[q][i] :
            board[p][i] = 2* x
            p = p +1
            x =0
          else :
            board[p][i] = x 
            p = p+1
            x = board[q][i]
        board[q][i] = 0
      if x != 0 :
        board[p][i] = x 
  
  #print(board)
  return board 

def move_down(board) :
  for i in range(N) :
    p = N-1
    x = 0
    for q in range(N-1, -1, -1):
      if board[q][i] == 0 :
        continue 
      if x == 0 :
        x = board[q][i]
      else :
        if x == board[q][i] :
          board[p][i] = 2 * x
          p = p -1
          x = 0
        else :
          board[p][i] = x 
          p = p-1 
          x = board[q][i]
      board[q][i] = 0
    if x != 0 :
      board[p][i] = x
  
  #print(board)
  return board 

def dfs(dfs_board, n) :
  if n == 5 :
    find_max(dfs_board)
    return 
  dfs(move_left(copy.deepcopy(dfs_board)), n+1)
  dfs(move_right(copy.deepcopy(dfs_board)), n+1)
  dfs(move_up(copy.deepcopy(dfs_board)), n+1)
  dfs(move_down(copy.deepcopy(dfs_board)), n+1)


if __name__ == '__main__':
  N = int(input())
  maxv = 0
  map_board = [list(map(int, input().split())) for _ in range(N)]
  dfs(map_board, 0)
  print(maxv)

===============================================================================
#1차시도 => 실패
from sys import stdin
from collections import deque

input = stdin.readline
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
#split() 활용해서 공백제거해서 인풋하기

#방향키 상하좌우
#최단거리? BFS

i = 0   #행부분 
j = 0   #열부분 
count = 0 
while count < 5:
  #print(a)

  if a[i][j] == a[i][j+1] : #열끼리 동일할경우
    tmp = int(a[i][j]*2)
    a[i][j+1]= tmp
    a[i][j] = 0 

    if i+1 == n : #리스트 오버플로우 방지
      count +=1 
      i = 0
    else :
      i+=1 
    continue 

  elif a[i][j] == a[i+1][j] : #행끼리 동일할경우
    tmp = int(a[i][j]*2)
    a[i+1][j] = tmp
    a[i][j] = 0 
    if j+1 == n :
      count +=1 
      j = 0
    else :
      j+=1 

    continue 
  else :
    #print("끝")
    break 

#print(a)
print(max(max(a)))
