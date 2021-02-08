# %%
import math

A, B, H, M = map(int, input().split())
total_M = H*60 + M

a_th = ((2*math.pi / 12) / 60) * total_M
b_th = (2*math.pi / 60) * total_M
a_rot = A*math.cos(a_th), A*math.sin(a_th)
b_rot = B*math.cos(b_th), B*math.sin(b_th)

print(math.sqrt((a_rot[0] - b_rot[0])**2 + (a_rot[1] - b_rot[1])**2))
