def prime(n):
    if n < 2:
        return False
    for i in range(2, n + 1):
        if n % i == 0:
            break
        else:
            return True