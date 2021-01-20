# %%
N = int(input())
S = input()
cur = S[0]
count = 1
for n in range(1, N):
    if S[n-1] != S[n]:
        count += 1
print(count)

# %%
