from yogi import read

def sieve_of_eratosthenes(n: int) -> list[bool]:
    """Returns a list, the sieve of Eratosthenes, with the first 
    n + 1 prime numbers."""

    assert n >= 2
    sieve = [False, False] + [True] * (n - 1)
    i = 2
    while i * i <= n:
        if sieve[i]:
            for j in range(2 * i, n + 1, i):
                sieve[j] = False
        i += 1
    return sieve

def main() -> None:
    # Gets the Sieve of Eratosthenes for the first n + 1 numbers, 
    # in this case we have 10^6 + 1 numbers.
    is_prime = sieve_of_eratosthenes(1000000)

    # Reads a sequence of natural numbers.
    x = read(int)
    while x is not None:
        if is_prime[x]:
            print(x, ' is prime', sep = '', end = '\n')
        else:
            print(x, ' is not prime', sep = '', end = '\n')
        x = read(int)

if __name__ == '__main__':
    main()