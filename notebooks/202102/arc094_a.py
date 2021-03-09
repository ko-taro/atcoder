# %%
a, b, c = sorted(list(map(int, input().split())))
count = c - b
diff = c - a - count
count += diff // 2
if diff % 2 == 1:
    count += 2

print(count)

# %%
a = [4, 1, 2, 3]
sorted(a)
a
