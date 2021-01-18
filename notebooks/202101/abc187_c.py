# %%
N = int(input())
ret = {}
out = 'satisfiable'
for i in range(N):
    Si = input()
    T = Si.lstrip('!')
    if T not in ret:
        ret[T] = {Si}
    else:
        ret[T] |= {Si}

        if len(ret[T]) >= 2:
            out = T
            break

print(out)

# %%
N = int(input())
S = set([input() for _ in range(N)])
S1 = set([s for s in S if '!' in s])
S2 =  S - S1
ret = set(map(lambda s: s.lstrip('!'), S1)) & S2
print(ret.pop() if len(ret) > 0 else 'satisfiable')

# %%
N = 6

S = """a
!a
b
!c
d
!d""".split('\n')
ret = set()
out = 'satisfiable'
count = 0
for i in range(N):
    Si = S[i]
    ret |= {Si}
    if count == len(ret):
        out = Si.lstrip('!')
        break
    count = len(ret)

print(out)

# %%
N = 6

S = """a
!a
b
!c
d
!d""".split('\n')
print(S)
ret = {}
for i in range(N):
    Si = S[i]
    if '!' in Si:
        T = Si[1:]
    else:
        T = Si

    if T in ret:
        ret[T] |= {Si}
    else:
        ret[T] = {Si}
    print(ret)

out = 'satisfiable'
for k, v in ret.items():
    if len(v) >= 2:
        out = k
        break

print(out)

# %%
S = set(range(10))
S1 = set(range(1, 10))
print(S - S1)