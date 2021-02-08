# %%
N, K = map(int, input().split())
h = sorted([int(input()) for _ in range(N)])
ret = [h[i+K-1] - h[i] for i in range(N-K+1)]
print(min(ret))

# %%
t = [3, 2, 1]
t.sort()

# %%
from datetime import datetime as dt
tdatetime = dt.now() # datetime型
tstr = tdatetime.strftime('%Y/%m/%d %H:%M:%S') # 文字列
tstr
# %%
from datetime import datetime as dt

tstr = '2012-12-29 13:49:37' # 文字列
tdatetime = dt.strptime(tstr, '%Y-%m-%d %H:%M:%S') # datetime型
tdatetime
# %%
from datetime import datetime as dt

tstr = '2012-12-29' # 文字列
tdatetime = dt.strptime(tstr, '%Y-%m-%d') # datetime型
tdate = tdatetime.date() # date型
# %%
tdate
# %%
from datetime import datetime as dt

tdate = dt.today() # date型
tstr = tdate.strftime('%Y/%m/%d') # 文字列
# %%
tstr
# %%
from datetime import datetime as dt

tdatetime = dt.now() # datetime型
tdate = tdatetime.date()

# %%
tdate
# %%
from datetime import datetime as dt

tdate = dt.today() # date型
tdatetime = dt(tdate.year, tdate.month, tdate.day) # datetime型
# %%
tdatetime.date()
# %%
