#백준X, 개인플젝 :)
#
#
#판크기 16*16 
#(5,5),(3,6),(7,2) 크기 가지는 박스를 최대 5개까지 테트리스 수행 

from sys import stdin

visited = [[0]* 16 for _ in range(16)] #판 크기를 초기화

num_list = {}
num =  list(stdin.readline()) 
#[(7,2),(7,2),(7,2),(7,2),(7,2)]
#입력값을 리스트로 초기화

flag = 0 
count = 0 
#리스트를 딕셔너리로 변환하는 과정
for i in num :
  if i != '[' and i != ']' and i != ',' and i != '(' and i != ')' and i != '\n' :
    if flag == 1 :
      flag = 0 
      num_list[count] = (int(tmp), int(i))
      count +=1 
    else : 
      flag = 1 
      tmp = i 
      #num_list[count]= i

print(num_list)
#{0: (5, 5), 1: (3, 6), 2: (7, 2), 3: (7, 2), 4: (7, 2)}


now_x, now_y = 15, 0 #현재위치

#입력받은크기만큼 반복문수행
for key,values in num_list.items() :
  x = values[0]
  y = values[1]
  cnt = 0
  if now_y + y <= 15 : 
    if visited[now_x - x][now_y + y] == 0 :
      for i in range(now_x, now_x - x, -1) :
        for j in range(now_y, now_y + y, +1 ) :
          visited[i][j] = 1 
    
    now_y += y
  else : #y축 오버플로우 발생 시
    for i in reversed(range(16)) :
      if visited[i][0] == 0 :
        now_y = 0
        now_x = i
        break 

    for i in range(now_x, now_x - x , -1 ) :
      for j in range(now_y, now_y +y, +1) :
        visited[i][j] = 1  
   
    now_y += y

  print(visited) 
  #break




