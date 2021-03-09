# %%
X, Y = map(int, input().split())

A = [X]
i = 1
while 2*A[i-1] <= Y:
    A.append(2*A[i-1])
    i += 1
print(len(A))

# %%
import math
X, Y = map(int, input().split())
i = math.floor(math.log2(Y/X))
print(i+1 if X*(2**i) <= Y else i)

# %%
math.floor(-3.1)