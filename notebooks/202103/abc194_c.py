# %%
N = int(input())
A = list(map(int, input().split()))

a1 = A[0]
a2 = A[0]**2
ret = 0
for i in range(1, N):
    ret += i*A[i]**2 -2 * A[i] * a1 + a2
    a1 += A[i]
    a2 += A[i]**2
print(ret)

# %%
# A[1]**2 - 2*A[1]*A[0] + A[0]**2
# 2 * A[2]**2 - 2*A[2]*(A[0] + A[1]) + (A[0]**2 + A[1]**2)
# (i, j)
# (2, 1) = (A2 - A1)^2 = A2**2 -2*A2*A1 - A1**2
# (3, 1), (3, 2) = 
# (4, 1), (4, 2), (4, 3)