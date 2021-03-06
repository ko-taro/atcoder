# %%
D, N = map(int, input().split())

print((100**D)*N if N != 100 else (100**D)*N + 100**D)

# %%
D, N = map(int, input().split())
p = 0
for i in range(1, N+1):
    p += 100**D
    if i % 100 == 0:
        p += 100**D
print(p)

# %%
# 1 100
# (100**1)*100 = 10,000 = 100**2 2回割り切れる
# だから、N = 100の時は、(100**1)*100 + 100**1 = 10,000 + 100 = 10,100
# D = 1の時は、3桁目を0にしないようにする