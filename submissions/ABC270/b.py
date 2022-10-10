def main():
    X, Y, Z = list(map(int, input().split()))
    if 0 < Y < X or X < Y < 0:
        if 0 < Z < Y or Y < Z < 0:
            res = abs(X)
        elif (Y > 0 and Z < 0) or (Y < 0 and Z > 0):
            res = abs(X) + abs(Z) * 2
        else:
            res = -1
    else:
        res = abs(X)
    print(res)


if __name__ == '__main__':
    main()
