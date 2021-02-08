# %%
N = int(input())
H = list(map(int, input().split()))
mem = [0]*N
flg = True
sub = 0
while True:
    count = 0
    for i in range(N-1):
        if H[i] <= H[i+1]:
            count += 1

        if H[i] - H[i+1] > 1:
            flg = False
            count = N-1
            break

        if H[i+1] < H[i]:
            if mem[i] == 0:
                H[i] -= 1
                mem[i] += 1
            else:
                flg = False
                count = N-1
                break
    if count == N-1:
        break

print('Yes' if flg else 'No')
