# %%
A = int(input())
B = int(input())
C = int(input())
X = int(input())

ret = 0
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            if X == 500*a + 100*b + 50*c:
                ret += 1
print(ret)

# %%
import itertools

A = int(input())
B = int(input())
C = int(input())
X = int(input())

ret = 0
combinations = itertools.product(range(A+1), range(B+1), range(C+1))
for a, b, c in combinations:
    if X == 500*a + 100*b + 50*c:
        ret += 1
print(ret)

# %%
import itertools

A = int(input())
B = int(input())
C = int(input())
X = int(input())

combinations = itertools.product(range(A+1), range(B+1), range(C+1))
print(sum([X == 500*a + 100*b + 50*c for a, b, c in combinations]))

# %%
A = int(input())
B = int(input())
C = int(input())
X = int(input())

ret = 0
for a in range(A+1):
    a_remain = X - 500*a
    if a_remain >= 0:
        for b in range(B+1):
            b_remain = a_remain - 100*b
            if b_remain >= 0 and b_remain // 50 <= C:
                ret += 1
print(ret)

# %%
import itertools
sample_a = ([1,2,3],[4,5,6],[7,8])
list_product = list(itertools.product(*sample_a))
print(list_product)