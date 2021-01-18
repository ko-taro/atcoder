# %%
N = int(input())
H = list(map(int, input().split()))
count = 0
maxc = 0
for i in range(1, N):
    if H[i-1] >= H[i]:
        count += 1
        if maxc < count:
            maxc = count
    else:
        count = 0
print(maxc)

# %%
N = int(input())
H = list(map(int, input().split()))
print(max(map(len, ''.join(['1' if H[i-1] >= H[i] else '0' for i in range(1, N)]).split('0'))))

# %%
max(map(int, ['1', '2']))