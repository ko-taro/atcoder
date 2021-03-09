# %%
H, W = map(int, input().split())

s = []
for h in range(H):
    s.append(input())

ret = True
for h in range(H):
    for w in range(W):
        cur = s[h][w]
        if cur == '#':
            tmp_ret = False
            tmp_ret |= w-1 >= 0 and s[h][w-1] == '#'
            tmp_ret |= w+1 <= W-1 and s[h][w+1] == '#'
            tmp_ret |= h-1 >= 0 and s[h-1][w] == '#'
            tmp_ret |= h+1 <= H-1 and s[h+1][w] == '#'
            ret &= tmp_ret
            if not ret:
                break
    if not ret:
        break

print('Yes' if ret else 'No')

# %%
t = [0]
False and t[1]

# %%
tmp_ret = False
tmp_ret |= True
tmp_ret
# %%
def check(h, w, H, W, s):
    tmp_ret = False
    x, y = 0, -1
    for _ in range(4):
        tmp_ret |= 0 <= h+x <= H-1 and 0 <= w+y <= W-1 and s[h+x][w+y] == '#'
        x, y = -y, x
    return tmp_ret

H, W = map(int, input().split())

s = [input() for _ in range(H)]

ret = [check(h, w, H, W, s) for h in range(H) for w in range(W) if s[h][w] == '#']

print('Yes' if sum(ret)==len(ret) else 'No')

# %%
H, W = map(int, input().split())
s = [input() for _ in range(H)]
check = lambda hx, wy: 0 <= hx <= H-1 and 0 <= wy <= W-1 and s[hx][wy] == '#'
ret = [check(h, w+1)|check(h, w-1)|check(h+1, w)|check(h-1, w) for h in range(H) for w in range(W) if s[h][w] == '#']
print('Yes' if sum(ret)==len(ret) else 'No')

# %%
s = """#.#.#
.#.#.
#.#.#
.#.#.
#.#.#""".split('\n')
[s[h][w] for h in range(5) for w in range(5) if s[h][w] == '#']

# %%
A = 'a'
f = lambda x: A
f(1)

