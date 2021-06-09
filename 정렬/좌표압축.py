#백준18870 좌표압축
#입력값에 따른, 본인보다 작은 수 개수 구하기
#
#시간초과 발생이유 = 이중for문... 딕셔너리 활용하자!
#

num = input()
list_num = list(map(int, input().split()))
sort_list = sorted(set(list_num))
answer = {x : y for y, x in enumerate(sort_list)}
#print(answer)
for i in list_num :
    print(answer[i], end=" ") # \n 대신 다른것으로 출력!!


=========================================
#1차시도 시간초과발생

num = input()
list_num = list(map(int, input().split()))
sort_list = sorted(set(list_num))
answer = []
for i in list_num :
    for idx, j in enumerate(sort_list) :
        if j >= i :
            answer.append(str(idx))
            break


print(' '.join(answer))

