#!/usr/bin/env python3

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def main():
    primes = [n for n in range(1, 31) if is_prime(n)]
    print("Prime numbers from 1 to 30:")
    print(" ".join(map(str, primes)))


if __name__ == '__main__':
    main()
