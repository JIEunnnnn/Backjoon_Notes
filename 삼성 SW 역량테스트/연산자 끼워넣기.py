#백준14888 연산자 끼워넣기
#주어진 숫자와 연산자에 따라 최댓값 최솟값 찾기
#
#1차시도때 규칙이 있는 줄알고 계산하다가 아니라는것을 깨달음
#2차시도때, deque로 연산자순서변경해가며 계산시도 => 숫자가아닌 연산자는 숫서뒤죽박죽이가능하다 ==> 순열..!! 

from sys import stdin
from itertools import permutations
#from collections import deque


size =  int(stdin.readline()) #숫자갯수
n = list(map(int, stdin.readline().split())) #숫자
num = list(map(int, stdin.readline().split())) #연산자 갯수

op_list = []
answer_list = []
op_list.extend(['+']*num[0])
op_list.extend(['-']*num[1])
op_list.extend(['x']*num[2])
op_list.extend(['/']*num[3])
opperand_list = set(permutations(op_list))

tmp = n.pop(0)
for i in opperand_list :
  tmp_answer = tmp
  for j in range(size-1) :
    if i[j] == '+' :
      tmp_answer += n[j]
    elif i[j] == '-' :
      tmp_answer -= n[j]
    elif i[j] == 'x' :
      tmp_answer *= n[j]
    elif i[j] == '/' :
      tmp_answer = int(tmp_answer/n[j])
  
  answer_list.append(tmp_answer)

#print(answer_list)
print(max(answer_list))
print(min(answer_list))

======================================================================
#1차시도
from sys import stdin
import copy


size =  int(stdin.readline()) #숫자갯수
n = list(map(int, stdin.readline().split())) #숫자
num = list(map(int, stdin.readline().split())) #연산자 갯수 
n2 = copy.deepcopy(n)
num2 = copy.deepcopy(num)

def max_def(size,n,m) :
  answer = n.pop(0) 
  #덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수
  for i in n :
    #최댓값 순서
    if m[1] != 0 :
        answer = answer - i 
        m[1] = m[1] -1 
    else :
      if m[3] != 0 :
        if answer > 0 :
          answer = int(answer / i) 
        else :
          answer = 0 
        m[3] = m[3] - 1 
      else :
        if m[0] != 0 :
          answer = answer + i
          m[0] = m[0] -1
        else :
          if m[2] != 0 :
            answer = int(answer * i )
            m[2] = m[2] - 1

  print(answer)         
  
def min_def(size, n, m) :
  answer = n.pop(0)
  #덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수
  for i in n :
    #최솟값 순서
    if m[0] != 0 :
        answer = answer + i 
        m[0] = m[0] -1 
    else :
      if m[3] != 0 :
        if answer > 0 :
          answer = int(answer / i) 
        else :
          answer = 0 
        m[3] = m[3] - 1 
      else :
        if m[1] != 0 :
          answer = answer - i
          m[1] = m[1] -1
        else :
          if m[2] != 0 :
            answer = int(answer * i )
            m[2] = m[2] - 1
    
    print(answer)
    print(m)
    print(i)
  print(answer)
  #return answer         




#num2 = num 얕은복사이므로 주소값을 가리킴 => 값바뀌면 같이 영향ㅇㅇ 
min_answer, max_answer = 0, 0
max_def(size,n,num)
min_def(size,n2,num2)



