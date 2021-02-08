# %%
N = int(input())
suma = sum(map(int, input().split()))
print(suma - N)

# %%
import math
N = int(input())
a = list(map(int, input().split()))
m = math.prod(a) - 1
fi = lambda ai: m % ai
print(sum(map(fi, a)))

# %%
N = int(input())
