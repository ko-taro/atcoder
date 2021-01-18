# %%
N = list(map(int, input()))
r = sum(N) % 3
c = 0
if r > 0:
    N = [n%3 for n in N]
    if N.count(r) == 0:
        t = 1 if r==2 else 2
        if N.count(t) >= 2 and len(N) >= 3:
            c = 2
        else:
            c = -1
    else:
        if len(N) >= 2:
            c = 1
        else:
            c = -1
print(c)

# %%
N = list(map(int, input()))
r = sum(N) % 3
c = 0
if r > 0:
    N = [n%3 for n in N]
    t = 1 if r==2 else 2
    if N.count(r) > 0 and len(N) > 1:
        c = 1
    elif N.count(t) > 1 and len(N) > 2:
        c = 2
    else:
        c = -1

print(c)

# %%
import numpy as np

N = np.array(list(map(int, input())))
r = np.sum(N) % 3
c = 0
if r > 0:
    t = 1 if r==2 else 2
    N = np.mod(N, 3)
    if np.count_nonzero(N==r) >= 1 and len(N) >= 2:
        c = 1
    elif np.count_nonzero(N==t) >= 2 and len(N) >= 3:
        c = 2
    else:
        c = -1
print(c)
        
# %%
import collections

N = list(map(int, input()))
r = sum(N) % 3
c = 0
if r > 0:
    t = 1 if r==2 else 2
    N = [n%3 for n in N]
    counter = collections.Counter(N)
    if counter[r] >= 1 and len(N) >= 2:
        c = 1
    elif counter[t] >= 2 and len(N) >= 3:
        c = 2
    else:
        c = -1
print(c)

# %%
count = 0
for n in range(1, int(10e5)):
    list_n = list(map(int, str(n)))
    modn = n % 3
    mod_list_n = sum(list_n) % 3
    if modn == mod_list_n:
        count += 1
count
# %%
len(range(1, int(10e5)))