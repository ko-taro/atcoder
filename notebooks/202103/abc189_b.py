# %%
N, X  = map(int, input().split())
nonda = 0
ret = -1
X = X*100
for i in range(N):
    Vi, Pi = map(int, input().split())
    nonda += Vi * Pi
    if nonda > X:
        ret = i + 1
        break
print(ret)
