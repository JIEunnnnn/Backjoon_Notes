#백준11720 숫자의 합 
#주어진 숫자를 합하는 문제
#
#int, str 변환하는 게 관건이지않을까? 
#

size, num = int(input()), input()
#print(ord(a))
answer = 0

for i in range(size) :
    answer += int(num[i])


print(answer)
