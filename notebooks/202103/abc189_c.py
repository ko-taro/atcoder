# %%
N = int(input())
A = list(map(int, input().split()))

ret = 0
for l in range(N):
    base = A[l]
    tmp_ret = base
    for r in range(l+1, N):
        if base > A[r]:
            break
        tmp_ret += base
    ret = max(ret, tmp_ret)
print(ret)

# %%
import numpy as np
def mikan(A, ret):
    if len(A) == 1:
        ret.append(A[0])
        return ret

    # 対象のリストで最小値をとるインデックスを取得
    min_idx = np.argmin(A)

    # 最小値を利用してみかんの個数を算出
    count = len(A) * A[min_idx]

    ret.append(count)

    # 最小値をとるインデックスを利用してリストを分割（ここで利用した最小値は含めないで、境界として利用する）
    left, right = A[:min_idx], A[min_idx+1:]
    if len(left) > 0:
        mikan(left, ret)

    if len(right) > 0:
        mikan(right, ret)

    return ret

N = int(input())
A = np.array(list(map(int, input().split())))
# A = np.random.randint(1, 10**5, 10**4)
ret = mikan(A, [])
print(max(ret))

# %%
import numpy as np

N = int(input())
A = np.array(list(map(int, input().split())))

targets = [A]
i = 0
ret = 0
while len(targets) > i:
    target = targets[i]

    # 対象のリストで最小値をとるインデックスを取得
    min_idx = np.argmin(target)

    # 最小値を利用してみかんの個数を算出
    count = len(target) * target[min_idx]

    ret = max(ret, count)

    # 最小値をとるインデックスを利用してリストを分割（ここで利用した最小値は含めないで、境界として利用する）
    left, right = target[:min_idx], target[min_idx+1:]

    if len(left) > 0:
        targets.append(left)
    if len(right) > 0:
        targets.append(right)

    i += 1

print(ret)

# %%
A = np.random.randint(1, 10, 5)
A
# %%
# 8, 6, 3, 3, 4
# argminは、2（3つ目の3が最小として出てくる）
# 3 * 5 = 15がこの場合のみかんの個数
# まずは、この15を記録する
# 次に、この最小値を境界として数列を二つに分割する
# そうすると、[8, 6]と[3, 4]になる
# それぞれに、対して同じようにargminをとって、最小値を計算し、argminを境界としてまた数列を分割する
# 例えば、[8, 6] -> argmin = 1 -> 6*2 = 12 -> [8], []に分割 -> 8個と0個
# [3, 4]に対しても -> argmin = 0 -> 3*2 = 6 -> [], [4] -> 0個と4個
# 結果として、みかんの個数は、15個、12個、8個、4個となる。
# だから、最大値は、15個
# ポイントは、最小値を境界として数列を2分割するところ。最小値だから、ここを跨いで計算することはないから分割して計算できる。
