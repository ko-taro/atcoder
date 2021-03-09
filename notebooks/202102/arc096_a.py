# %%
a, b, c, x, y = map(int, input().split())

ab_val = a*x + b*y
mix_val = min(x, y) * 2 * c + max((x-y)*a, (y-x)*b)
c_val = max(x, y) * 2 * c
print(min(ab_val, mix_val, c_val))

# %%
a, b, c, x, y = map(int, input().split())

ab_val = a*x + b*y
mix_val = 2 * c * (x if x < y else y) + ((x-y)*a if x > y else (y-x)*b)
c_val = 2 * c * (x if x < y else y)
print(min(ab_val, mix_val, c_val))

# %%
a+b, 2*c
# a+bの方が安ければ、全て個別で買った方が安い
# 2*cの方が安ければ、AとB同じ枚数を買うのであればABで買った方が安い
# 2*cの方が安いパターンは、AとBのどちらかが多い場合に分岐する。
# A > Bの場合を考える。AピザとBピザをB枚づつ買うのは、ABピザを買うのが安い。
# 残り、Aピザを（A-B)枚買う金額は、Aピザを1枚用意する単価によって金額が変わる
# 1. Aピザを1枚買う場合
# 2. ABピザを2枚買う
# つまり、A < 2*cであれば、Aで揃えた方が良くて、A > 2*cであれば、ABピザで揃えた方が良い