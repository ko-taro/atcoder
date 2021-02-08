# %%
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

damage = 0
for i in range(N):
    d1 = min(A[i], B[i])
    B[i] -= d1

    d2 = min(A[i+1], B[i])
    A[i+1] -= d2

    damage += d1 + d2

print(damage)

# %%
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

damage = 0
for i in range(N):
    d1 = B[i] if A[i] > B[i] else A[i]
    B[i] -= d1

    d2 = B[i] if A[i+1] > B[i] else A[i+1]
    A[i+1] -= d2

    damage += d1 + d2

print(damage)
