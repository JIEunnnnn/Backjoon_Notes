#백준2675 문자열 반복
#주어진 입력값에 따라 문자열 반복되는 값 출력
#
#리스트로 append 시켜서 한꺼번에 출력..!
#

num = int(input())
list_answer = []
for i in range(num) :
    n = input().split()

    answer = ''
    cnt = int(n[0])
    for i in n[1] :
        answer += cnt * i
    list_answer.append(answer)

for i in list_answer :
    print(i)
