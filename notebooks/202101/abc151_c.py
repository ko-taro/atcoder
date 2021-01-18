# %%
N, M = map(int, input().split())

ans = ['']*N
for i in range(M):
    p, s = input().split()
    p = int(p)
    if '1' not in ans[p-1]:
        ans[p-1] += '1' if s == 'AC' else '0'

acs = [a for a in ans if '1' in a]
ret = ''.join(acs)

print(len(acs), len(ret.replace('1', '')))

# %%
2 5
1 WA
1 AC
2 WA
2 AC
2 WA
# %%
'abs'.replace('b', '')