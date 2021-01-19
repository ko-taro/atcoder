# %%
N = int(input())
A = list(map(int, input().split()))

A = [[A[i], i] for i in range(len(A))]
while len(A) > 2:
    tmp = []
    for i in range(0, len(A)-1, 2):
        ret = A[i] if A[i][0] > A[i+1][0] else A[i+1]
        tmp.append(ret)
    A = tmp

print(A[0][1]+1 if A[0][0] < A[1][0] else A[1][1]+1)

# %%
N = int(input())
A = list(map(int, input().split()))

A = [[A[i], i] for i in range(len(A))]
for t in range(N-1):
    A = [A[i] if A[i][0] > A[i+1][0] else A[i+1] for i in range(0, len(A)-1, 2)]
print(A[0][1]+1 if A[0][0] < A[1][0] else A[1][1]+1)

# %%
N = int(input())
A = list(map(int, input().split()))

A = [[A[i], i] for i in range(len(A))]
def f(A):
    if len(A) <= 2:
        return A[0][1]+1 if A[0][0] < A[1][0] else A[1][1]+1
    return f([A[i] if A[i][0] > A[i+1][0] else A[i+1] for i in range(0, len(A)-1, 2)])

print(f(A))
