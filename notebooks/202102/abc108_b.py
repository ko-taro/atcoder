# %%
def rot90(v):
    return -v[1], v[0]

x1, y1, x2, y2 = map(int, input().split())

v = x2 - x1, y2 - y1

v = rot90(v)
x3, y3 = x2 + v[0], y2 + v[1]

v = rot90(v)
x4, y4 = x3 + v[0], y3 + v[1]

print(x3, y3, x4, y4)

# %%
x1, y1, x2, y2 = map(int, input().split())

v = x2 - x1, y2 - y1

cur = [x2, y2]
ret = []
for i in range(2):
    v = -v[1] , v[0]
    ret.append([cur[0] + v[0], cur[1] + v[1]])
    cur = ret[i]

print(sum(ret, []))

# %%
x1, y1, x2, y2 = map(int, input().split())
v = -(y2-y1), x2 - x1
print(x2 + v[0], y2 + v[1], x1 + v[0], y1 + v[1])

# %%
x1, y1, x2, y2 = map(int, input().split())
print(x2 -(y2-y1), y2 + x2 - x1, x1 -(y2-y1), y1 + x2 - x1)
