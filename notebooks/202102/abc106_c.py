# %%
S = input()
K = int(input())

if len(S) >= K and set(S[:K]) == {'1'}:
    print('1')
else:
    ret = '1'
    for i in range(len(S)):
        if S[i] != '1':
            ret = S[i]
            break
    print(ret)


# %%
'aa'.find('a')