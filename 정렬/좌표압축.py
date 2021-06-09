

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
