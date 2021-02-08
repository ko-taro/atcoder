# %%
N, M = map(int, input().split())
S = []
for i in range(N):
    A, B = map(int, input().split())
    S.append([A, B])

S = sorted(S, key=lambda x: x[0])
ret = 0
cur = 0
for i in range(N):
    if S[i][1] - (M - cur) >= 0:
        ret += (M - cur) * S[i][0]
        cur += (M - cur)
    else:
        ret += S[i][1] * S[i][0]
        cur += S[i][1]

    if cur == M:
        break
print(ret)

# %%
N, M = map(int, input().split())
S = []
for i in range(N):
    A, B = map(int, input().split())
    S.append([A, B])

S = sorted(S, key=lambda x: x[0])
ret = 0
i = 0
while S[i][1] - M < 0:
    ret += S[i][1] * S[i][0]
    M -= S[i][1]
    i += 1
ret += M * S[i][0]

print(ret)

# %%
# N, M = map(int, input().split())
# S = []
# for i in range(N):
#     A, B = map(int, input().split())
#     S.append([A, B])

# テスト
N, M = 4, 30
S = list(map(lambda x: list(map(int, x.split())), """6 18
2 5
3 10
7 9""".split('\n')))

S = sorted(S, key=lambda x: x[0])
ret = 0
i = 0
while S[i][1] - M < 0:
    ret += S[i][1] * S[i][0]
    M -= S[i][1]
    i += 1

ret += M * S[i][0]

print(ret)

# %%
a = [
    [1, 2],
    [-1, 5]
]
sorted(a, key=lambda x: x[0]), a