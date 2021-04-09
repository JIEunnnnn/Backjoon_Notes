#백준14501 퇴사
#최대이익출력하는 알고리즘구현 
#
#DP형식으로 구현...해야하는것.. 점화식...기억도안나는데ㅠㅠ
#https://jeongchul.tistory.com/671


from sys import stdin 

n = int(stdin.readline()) 

t, p = [0] * n, [0] * n 

for i in range(n):
  t[i], p[i] = map(int, stdin.readline().split())

dp = [0] * 25 
for i in range(n) :
  print(dp)
  if dp[i] > dp[i+1]:#현재보상이 다음날보다 클 경우
      dp[i+1] = dp[i] 

  if dp[i+t[i]] < dp[i] + p[i]: # 현재보상보다 t일후의 금액이 작을경우 
      #print(dp[i])
      #print(p[i])
      #print(dp[i+t[i]])
      dp[i+t[i]] = dp[i] + p[i] 
  

print(dp[n])




