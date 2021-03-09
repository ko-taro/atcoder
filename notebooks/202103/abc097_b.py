# %%
X = int(input())

maxv = 0
for b in range(1, 101):
    for p in range(2, 10):
        cur = b**p
        if cur > X:
            break
        maxv = max(cur, maxv)

print(maxv)

# %%
import math
X = int(input())

maxv = 0
for b in range(1, 101):
    maxp = math.floor(math.log(X) / math.log(b)) if b != 1 else 2
    if maxp > 1:
        print(b, maxp, b**maxp)
        maxv = max(b**maxp, maxv)
print(maxv)

# %%
# b^p <= X
# p logb <= log X
# p <= log X / log b