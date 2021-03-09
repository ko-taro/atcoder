# %%
N = int(input())
ret = True
for _ in range(N):
    t, x, y = map(int, input().split())
    if not (t >= x + y and (x + y) % 2 == t % 2):
        ret = False
        break

print('Yes' if ret else 'No')

# %%
N = int(input())
ret = True
tn, xn, yn = 0, 0, 0
for _ in range(N):
    tn1, xn1, yn1 = map(int, input().split())
    t = tn1 - tn
    x = abs(xn1 - xn)
    y = abs(yn1 - yn)
    if not (t >= x + y and (x + y) % 2 == t % 2):
        ret = False
        break
    tn = tn1
    xn = xn1
    yn = yn1
print('Yes' if ret else 'No')