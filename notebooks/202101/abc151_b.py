# %%
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

ret = max(N*M - sum(A), 0)
print(ret if ret <= K else -1)

# %%
5 10 7
8 10 3 6