# %%
# 出来なかった
import itertools

N = int(input())
L = list(map(int, input().split()))

ret = 0
for a, b, c in itertools.combinations(L, 3):
    if a < b + c and b < a + c and c < a + b:
        a_c = L.count(a)
        b_c = L.count(b)
        c_c = L.count(c)
        ret += a_c * b_c * c_c
print(ret)

# %%
import itertools
len(itertools.combinations(range(1000), 3))