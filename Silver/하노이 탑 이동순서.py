#백준11729 하노이 탑 이동순서
#이동횟수를 최소로하는 하노이탑 이동과정 출력하기 
#
#
#하노이탑은 재귀형식으로 풀어야한다는 것! 잊지말자!

from sys import stdin

def hanoi(n, start, end, assist, answer_list) :
    if n == 1:
        answer_list.append([start, end])
        return
    hanoi(n-1, start, assist, end,answer_list)
    answer_list.append([start, end])
    hanoi(n-1, assist, end, start,  answer_list)
    return


input = stdin.readline
n = int(input())
answer_list = []
hanoi(n,1,3,2,answer_list)
print(len(answer_list))
for i,j in answer_list :
    print(str(i) +" "+ str(j))
    
