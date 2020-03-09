#sからtへたどり着けるか
#頂点数vと辺の数e
v, e = map(int, input().split())
s, t = map(int, input().split())
graph = [[] for i in range(v)]
#辺の数だけ入力があり、e1とe2は連結していることを表す
for i in range(e):
  e1, e2 = map(int, input().split())
  #無向グラフのため、両方から行けること
  graph[e1].append(e2)
  graph[e2].append(e1)

print(graph)

seen = [False] * v

def dfs(g, v):
  seen[v] = True
  for next_v in g[v]:
    if seen[next_v]:
      continue
    dfs(g, next_v)
  
dfs(graph, s)

if seen[t]:
  print('Yes')
else:
  print('No')