# %%
N = int(input())
suma = sum(map(int, input().split()))
print(suma - N)

# %%
import math
N = int(input())
a = list(map(int, input().split()))
m = math.prod(a) - 1
print(sum(map(lambda ai: m % ai, a)))

# %%
N = int(input())
