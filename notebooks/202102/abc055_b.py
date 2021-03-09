# %%
N = int(input())

power = 1
th = int(1e9+7)
for i in range(N, 1, -1):
    power = (power * i) % th

print(power % th)
