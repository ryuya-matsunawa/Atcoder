def main():
    scores = [(0,), (1,), (2,), (1, 2), (4,), (1, 4), (2, 4), (1, 2, 4)]
    A, B = list(map(int, input().split()))
    A_B = tuple(scores[A]) + tuple(scores[B])
    A_B = set(A_B)
    res = sum(A_B)
    print(res)


if __name__ == '__main__':
    main()
