#백준13458 시험감독
#총감독과 부감독을 합친 최소감독 수 구하기
#
#1차시도때, while문으로 음수나올때까지 뺄셈시도 (시간초과)
#math 라이브러리 활용해서, 나눗셈 몫을 더하여 결과값 return 

from sys import stdin
import math 

n =  int(stdin.readline()) #시험장 개수
m = list(map(int, stdin.readline().split())) #각시험장의 응시자수
k, o = map(int, stdin.readline().split()) #총감독, 부감독이 감독할수있는 인원 수 

answer = 0


for i in m :
  tmp = i - k  
  answer += 1 
  #print(tmp)
  #print(answer)

  if tmp <= 0 :
    continue
  else :
    #print(tmp)
    cnt = math.ceil(tmp/o) 
    answer += cnt

print(answer)

===========================================================================
#1차시도 => 시간초과발생 
from sys import stdin

n =  int(stdin.readline()) #시험장 개수
m = list(map(int, stdin.readline().split())) #각시험장의 응시자수
k, o = map(int, stdin.readline().split()) #총감독, 부감독이 감독할수있는 인원 수 

answer = 0


for i in m :
  tmp = i - k  
  answer += 1 
  #print(tmp)
  #print(answer)

  if tmp <= 0 :
    continue
  else :
    #print(tmp)
    while tmp > 0 :
      tmp -= o 
      answer +=1 
      #print(answer)

print(answer)
    


