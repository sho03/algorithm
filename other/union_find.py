n,q = map(int,input().split())
pab = [list(map(int, input().split())) for _ in range(q)]

# 始め、全ての要素の親を自分自身とする
parent = list(range(n))

#親を見つける
def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

#xの一番上の親をyの親に設定する
def union(x,y):
    parent[find(x)]=find(y)

#x,yが同じ親を持つかチェック
def same(x,y):
    return find(x)==find(y)

for i,j,k in pab:
    if i==1:
        if same(j,k):
            print("Yes")
        else:
            print("No")
    else:
        union(j,k)
