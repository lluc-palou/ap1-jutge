from yogi import read

def is_perfect_prime(n: int) -> bool:
    """Determines if the given number is a perfect prime, in fact, the sum
    of his digits is prime in any given moment."""

    if n < 2:
        return False

    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1
    
    if n < 10:
        return True

    return is_perfect_prime(digits_sum(n))

def digits_sum(n: int) -> int:
    """Returns the sum of the digits of a given number."""

    if n < 10:
        return n
    else:
        return n % 10 + digits_sum(n // 10)

def main() -> None:
    # Reads a natural number.
    n = read(int)

    if is_perfect_prime(n):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()