# %%
S = input()

odd_s = S[::2]
even_s = S[1::2]

odd_1 = odd_s.count('1')
even_1 = even_s.count('1')

ret1 = odd_1 + (len(even_s) - even_1) # 010101にするカウント
ret2 = (len(odd_s) - odd_1) + even_1

print(min(ret1, ret2))

# %%
# odd_s：奇数番目の文字列
# odd_1：奇数番目の文字が1である数
# even_s：偶数番目の文字列
# even_1：偶数番目の文字列が1である数

# %%
'12345'[::2]
00101
10101
01010