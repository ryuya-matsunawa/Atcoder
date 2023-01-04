x = int(input())


def is_prime(n):
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True


while True:
    if is_prime(x):
        print(x)
        exit()
    else:
        x += 1
