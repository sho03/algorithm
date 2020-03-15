from collections import deque
#幅優先探索
#入力はN個の頂点とM個の辺、各辺0...m - 1はa(n)とb(n)をつないでいる
#n m
#a(0) b(0)
#a(1) b(1)
#......
#a(m - 1) b(m - 1) 

n, m = map(int, input().split())
graph = [[] for i in range(n)]
for i in range(m):
  a = list(map(int, input().split()))
  graph[a[0]].append(a[1])
  graph[a[1]].append(a[0])

#頂点vまで何ステップで到達できるかを記録する
dist = [-1] * n
#発見済、かつ未訪問の頂点を格納するキュー
q = deque()

#頂点0をスタート位置とするため、頂点0をキューに入れ、dist[0]は0ステップで到達可能とする
q.append(0)
dist[0] = 0

#キューに要素がある間続ける
while q:
  #キューの先頭から要素を取り出す
  v = q.popleft()

  for next_v in graph[v]:
    if not dist[next_v] == -1:
      continue
    dist[next_v] = dist[v] + 1
    q.append(next_v)

print(dist)