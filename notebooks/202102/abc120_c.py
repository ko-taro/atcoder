# %%
S = input()
c = S.count('0')
print(2*min(c, len(S)-c))
