import sys
sys.setrecursionlimit(10**6)

N, X, Y = list(map(int, input().split()))
answer = [X]
G = [[] for _ in range(N)]


def main():
    for _ in range(N - 1):
        u, v = list(map(int, input().split()))
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    search(X - 1, -1)


def search(pos, bef):
    if pos + 1 == Y:
        print(*answer)
        exit()
    for to in G[pos]:
        if to != bef:
            answer.append(to + 1)
            search(to, pos)
            answer.pop()
    return


if __name__ == '__main__':
    main()
