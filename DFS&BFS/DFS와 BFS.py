#백준1260. DFS와 BFS
#양방향 그래프를 정점 작은순으로 방문하는 알고리즘 구현 
#
#DFS와 BFS의 개념 다시한번더 상기..!
#

import sys
from collections import deque
input = sys.stdin.readline

#그래프, 시작시점
def BFS(graph, root) :
  visited = []
  queue = deque([root])

  while queue :
    n = queue.popleft()

    if n not in visited :
      visited.append(n)
      if n in graph :
        temp = list(set(graph[n]) - set(visited))
        #양방향이기 때문에 중복제거하기 위한것

        temp.sort()
        #정점이 작은수부터 방문!
        queue += temp
        #queue += graph[n] - set(visited)
  return " ".join(str(i) for i in visited) 
  #리스트를 string으로 변환 
  


def DFS(graph, root ) :

  visited = []
  stack = [root]

  while stack :

    n = stack.pop()

    if n not in visited :
      visited.append(n)
      if n in graph:
            temp = list(set(graph[n]) - set(visited))
            temp.sort(reverse=True)
            #스택이니까 reverse... 
            #정점이 작은수부터 방문! 
            #top[-1]

            stack += temp
            #stack += graph(n) - set(visited)
  
  return " ".join(str(i) for i in visited)





n = input().split(' ')
node, edge, start = [int(i) for i in n]
graph = {}


for i in range(edge):
    edge_info = input().split(' ')
    n1, n2 = [int(j) for j in edge_info]
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

#print(graph)
#{1: [2, 3, 4], 2: [1, 4], 3: [1, 4], 4: [1, 2, 3]}

print(DFS(graph, start))
print(BFS(graph, start))
