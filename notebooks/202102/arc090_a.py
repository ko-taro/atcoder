# %%
N = int(input())
A = [list(map(int, input().split())) for i in range(2)]

max_ame = 0
for i in range(N):
    max_ame = max(max_ame, sum(A[0][0:i+1]) + sum(A[1][i:]))

print(max_ame)

# %%
N = int(input())
A = [list(map(int, input().split())) for i in range(2)]

print(max([sum(A[0][0:i+1]) + sum(A[1][i:]) for i in range(N)]))

# %%
A[0][0:N-1]

# %%
A = [
    [1, 2, 3],
    [4, 5, 6]
]
print(A[1][1:3])

# %%
l = [1, 2, 3, 4, 5]
l2 = []
for li in l:
    l2.append(li**2)
print(l2)
# %%
%%time
l = list(range(1000))
l2 = list(filter(lambda x: x%2 == 0, l))
# %%
%%time
l = list(range(1000))
l2 = [li for li in l if li % 2 == 0]
# %%
from functools import reduce
l = list(range(10))
reduce(lambda x, y: x+y, l)

# %%
from functools import reduce

def add(x, y):
    print(x, '+',  y, '=', x+y)
    return x+y

l = list(range(1, 11))
print(reduce(add, l, 0))
