#백준2941 크로아티아 알파벳
#크로아티아 알파벳 개수 + 일반알파벳 개수 구하기
#
#stack을 활용했는데 예외처리하는것 까먹지말기!! (stack이 남아있을경우!!)
#

from collections import deque


croati = ['c=','c-','dz=','d-','lj','nj','s=','z=']
dicted  = { c : 0 for c in croati}
#print(dicted)

n = input()
stack = ''
cnt = 0
for i in n :
    stack += i
    if len(stack) >= 2:
        if stack in dicted :
            dicted[stack] +=1
            stack = ''
        else :
            if len(stack) >= 3 :
                stack =stack[1:]
                cnt +=1

            if stack in dicted:
                dicted[stack] += 1
                stack = ''



print(sum(dicted.values())+cnt+len(stack))
