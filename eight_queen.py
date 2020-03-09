#盤面の1辺のマス数
n = int(input()) 

pos = [-1] * n
col = [False] * n
down = [False] * (2 * n - 1)
up = [False] * (2 * n - 1)

def print_queens():
  for i in range(n):
    for j in range(n):
      if pos[i] == j:
        print('Q', end=" ")
      else:
        print('*', end=" ")
    print("")

def test(a):
  for b in range(n):
    if not col[b] and not up[a + b] and not down[a - b + (n - 1)]:
      pos[a] = b
      col[b] = True
      up[a + b] = True
      down[a - b + (n - 1)] = True

      if a + 1 >= n:
        return True
      else:
        if test(a + 1):
          return True
        else:
          pos[a] = -1
          col[b] = False
          up[a + b] = False
          down[a - b + (n - 1)] = False
  return False        

if test(0):
  print_queens()
else:
  print("fail")