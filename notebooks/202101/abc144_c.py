# %%
import math
N = int(input())
minv = N - 1
for i in range(2, math.ceil(math.sqrt(N))+1):
    if N % i == 0:
        d = i - 1 + (N // i) - 1
        if d < minv:
            minv = d
print(minv)

# %%
N = int(input())
minv = N - 1
for i in range(int(N**0.5), 1, -1):
    if N % i == 0:
        d = i - 1 + (N // i) - 1
        if d < minv:
            minv = d
        elif d >= minv:
            break

print(minv)

# %%
N = int(input())
for i in range(int(N**0.5), 1, -1):
    if N % i == 0:
        maxn = i
        break
print(maxn - 1 + (N // maxn) - 1)












