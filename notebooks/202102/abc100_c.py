# %%
N = int(input())
a = list(map(int, input().split()))
count = 0
for ai in a:
    while ai % 2 == 0:
        ai = ai // 2
        count += 1
print(count)

# %%
# 5 2 4 = 5 2^1 2^2
# 2の指数部分の和を求める

# %%
4 >> 1
# %%
N = int(input())
a = list(map(int, input().split()))
count = 0
for ai in a:
    while ai % 2 == 0:
        ai = ai >> 1
        count += 1
print(count)

# %%
a = 4 >> 1
a