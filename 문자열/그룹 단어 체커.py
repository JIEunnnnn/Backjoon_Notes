#백준1316 그룹 단어 체커
#그룹단어의 개수는 몇개인가? (중복은 허용하다 연속해야함)
#
#예외처리하는 것 제외하고는 어렵지않았다! 
#

import string
import copy

n = int(input())
words = []
for i in range(n) :
    words.append(input())

alphas = {i : True for i in string.ascii_lowercase }
answer = 0
for word in words :
    alpha = copy.deepcopy(alphas)
    #print(alpha)
    flag = True
    tmp = ''
    for w in word :
        if tmp == w :
            continue
        else :
            if alpha[w] :
                alpha[w] = False
                tmp = w
            else :
                #print(w)
                flag = False
                break


    if flag :
        #print(word)
        answer +=1

print(answer)




