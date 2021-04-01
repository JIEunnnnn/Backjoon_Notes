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
