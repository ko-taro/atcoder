# %%
S = 'ACCb'
ret = S[0] == 'A' \
    and S[2:len(S)-1].count('C') == 1 \
    and all(list(map(lambda s: s.islower(), S[1:].split('C'))))
print('AC' if ret else 'WA')

# %%
S = input()
ret = S[0] == 'A' \
    and S[2:len(S)-1].count('C') == 1 \
    and S[1:].replace('C', '').islower() # 2文字目と末尾がCであった場合AC出してしまう
print('AC' if ret else 'WA')

# %%
list(map(lambda s: s.islower(), S[1:].split('C')))

# %%
t = '12345'
t = [True, True, True]
sum(t)  == len(t)