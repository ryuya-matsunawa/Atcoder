N, K = map(int, input().split())
A = list(map(int, input().split()))

# x周した時に食べるのリンゴの数がK個以上か


def check(x):
    cnt = 0
    for a in A:
        # a > x => 周回数より残っているリンゴの数の方が多い
        # x > a => リンゴより周回数の方が多い
        cnt += min(a, x)
    return cnt >= K


# リンゴを食べ切る周回数 - 1を求める
ok = max(A) + 1
ng = -1
# 最大周と最小周の差が1になったら終わる（最小周がリンゴを食べ切る周回数 - 1になる）
while ok - ng > 1:
    # 最大周と最小周を足して2で割る
    mid = (ok + ng) // 2
    # mid周でリンゴを食べ切る場合は最大周を更新
    if check(mid):
        ok = mid
    else:
        ng = mid

# 最終周前までリンゴの数を減らす
for i in range(N):
    # A[i]個か周回数の少ない方を総数から減らす
    K -= min(A[i], ng)
    # A[i] - 周回数が正ならリンゴが残る
    A[i] = max(0, A[i] - ng)

# ラスト1周
for i in range(N):
    if K == 0:
        break
    if A[i] > 0:
        K -= 1
        A[i] -= 1

print(*A)
