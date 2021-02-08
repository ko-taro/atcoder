# %%
N = int(input())
h = list(map(int, input().split()))

count = 0
def searchl(h):
    for k in range(len(h)):
        if h[k] != 0:
            return k
    return None

while True:
    k0 = searchl(h)
    if k0 is None:
        break

    for k in range(k0, len(h)):
        if h[k] != 0:
            h[k] -= 1
        elif h[k] == 0:
            break
    count += 1

print(count)

# %%
N = int(input())
h = list(map(int, input().split()))

count = 0
while True:
    l, r = None, len(h)
    for k in range(len(h)):
        if l is None and h[k] != 0:
            l = k
        elif l is not None and h[k] == 0:
            r = k
            break

    if l is None:
        break
    
    for k in range(l, r):
        h[k] -= 1

    count += 1

print(count)

# %%
t = [1, 2, 3]
map(lambda x: x-1, t[0:2])