# %%
# WRが無くなるよう操作する
# WRRRRのようにWの右隣にRが連続する場合は、非効率なことがある？
# WRR...Rが非効率な場合はどのような時だろうか？
# WRWWRRWRR
# RRWWRRWRW
# 
# WRWWRWRR
# RRWWRWRW
# RRWWRWRW

# WRRRRWWR -> 1
# WWRRRRWWR -> 2
# WWRRRRWWRR
# WWWRR
# WRRRRWWRR

# %%
# N = int(input())
# C = input()
C = 'RWRWRWRR'

ret = 0
if C.count('WR') != 0:
    C = C.lstrip('R')
    countr = C.count('R')

    firstr = C.find('R')

    firstr2 = firstr
    for i in range(firstr, len(C)):
        if C[i] != 'R':
            firstr2 = i - 1
            break
    
    firstw_cnt = firstr
    firstr_cnt = firstr2 - firstr + 1
    remainr_cnt = countr - firstr_cnt

    if firstw_cnt <= remainr_cnt:
        ret += remainr_cnt
    else:
        ret += firstw_cnt if firstw_cnt <= countr else countr

print(ret)
# %%
N = int(input())
C = input()

countr = C.count('R')
print(C[0:countr].count('W'))

# %%
s = 'RRRWRWRW'
for i in range(len(s)-1, -1, -1):
    print(s[i])
