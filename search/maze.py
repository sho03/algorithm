from collections import deque
#幅優先探索を利用した迷路の最短経路を解く
#入力はx, y が迷路の幅と高さ、その後に迷路の図が入力される
"""
8 8
.#....#G
.#.#....
...#.##.
#.##...#
...###.#
.#.....#
...#.#..
S.......
"""
x, y = map(int, input().split())
#迷路の入力
field = [list(input()) for i in range(y)]

#スタートとゴールの位置を確認する
start_x = start_y = 0
goal_x = goal_y = 0
for i in range(x):
  for j in range(y):
    if field[i][j] == 'S':
      start_x = i 
      start_y = j
    if field[i][j] == 'G':
      goal_x = i
      goal_y = j

#探索開始前の準備
#各セルの最短距離
dist = [[-1] * x for i in range(y)]
#スタート位置は0ステップ
dist[start_x][start_y] = 0
#キューを生成（発見済かつ未訪問の頂点）
q = deque()
q.append((start_x, start_y))

#移動方向4か所(右、上、左、下)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

prev_x = [[-1] * x for i in range(y)]
prev_y = [[-1] * x for i in range(y)]

#幅優先探索の開始
while q:
  current_pos = q.popleft()
  current_x = current_pos[0]
  current_y = current_pos[1]

  for i in range(4):
    next_x = current_x + dx[i]
    next_y = current_y + dy[i]

    if next_x < 0 or next_x >= x or next_y < 0 or next_y >= y:
      #場外アウト
      continue
    if field[next_x][next_y] == '#':
      #壁の場合
      continue
    #未訪問の地点はキューに追加
    if dist[next_x][next_y] == -1:
      q.append((next_x, next_y))
      dist[next_x][next_y] = dist[current_x][current_y] + 1
      prev_x[next_x][next_y] = current_x
      prev_y[next_x][next_y] = current_y

print('shortest root is ...')      
print(dist[goal_x][goal_y])
print('')

g_x = goal_x
g_y = goal_y
while g_x != -1 and g_y != -1:
  if not field[g_x][g_y] == 'S' and not field[g_x][g_y] == 'G':
    field[g_x][g_y] = '○'
  px = prev_x[g_x][g_y]
  py = prev_y[g_x][g_y]
  g_x = px
  g_y = py

print('root')
for i in range(x):
  for j in range(y):
    print(field[i][j], end=' ')
  print('')