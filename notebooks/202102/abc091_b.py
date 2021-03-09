# %%

N = int(input())
ss = [[1, input()] for _ in range(N)]
strs = set([s[1] for s in ss])

M = int(input())
ts = [[-1, input()] for _ in range(M)]

merged = ss + ts
max_val = 0
for target in strs:
    ret = sum([s[0] for s in merged if s[1] == target])
    max_val = max(ret, max_val)

print(max_val)

# %%
N = int(input())
ss = [input() for _ in range(N)]
strs = set(ss)

M = int(input())
ts = [input() for _ in range(M)]

max_val = max([max(ss.count(target) - ts.count(target), 0) for target in strs])
print(max_val)

# %%
N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]

tmp = set(S[0])
money = 0

for s in set(S):
    print(s, tmp)
    print(S.count(s), S.count(tmp))
    if S.count(s) >= S.count(tmp):
        # print(s, tmp)
        if S.count(s) > T.count(s):
            tmp = s

money += S.count(tmp) - T.count(tmp)

print(money)

# %%
# 1 / 素数の和
import numpy as np

N = 10000000

primes = np.arange(2, N+1)

p = 2
while p <= np.floor(np.sqrt(N)):
    primes = primes[(np.mod(primes, p) != 0) | (primes == p)]
    p = np.min(primes[primes > p])

print(sum(1 / primes))
# %%
len(primes)