

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



