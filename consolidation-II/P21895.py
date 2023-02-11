from yogi import scan

def number_lenght(n: int) -> int:
    """Returns the lenght of the number."""

    l = 0

    while n > 9:
        n = n // 10
        l += 1
    return l + 1

def last_number(n: int) -> int:
    """Returns the last number of a given number."""

    if n < 10:
        return n

    else:
        return n % 10

def non_strobogrammatic_numbers(n: int) -> bool:
    """Determines if the given natural number can't be strobogrammatic having into account
    that has non-strobogramatic numbers, otherwise could be strobogrammatic."""

    while n > 9:
        if last_number(n) != 1 and last_number(n) != 6 and last_number(n) != 8 and last_number(n) != 9 and last_number(n) != 0:
           return True
        else:
            n = n // 10
    
    if n < 10:
        if n != 1 and n != 8 and n != 6 and n != 9 and n != 0:
           return True
    
    return False

def upside_downside_equal(n: int) -> bool:
    """Determines if the number is the same seen upside and downside."""
    m = n
    x = 0

    while n > 9:
        if last_number(n) == 6:
            x = x * 10 + 9
        elif last_number(n) == 9:
            x = x * 10 + 6
        else:
            x = x * 10 + last_number(n)
        n = n // 10

    if n == 6:
        x = x * 10 + 9
    elif n == 9:
        x = x * 10 + 6
    else:
        x = x * 10 + n
    
    if x != m:
        return False
    else:
        return True

def is_strobogrammatic(n: int) -> bool:
    """Says if a given natural number is strobogrammatic."""

    # The number ends with 0, hence is not strobogrammatic.
    if n > 9 and last_number(n) == 0:
        return False
    
    # The number has non-strobogrammatic numbers, hence is not strobogrammatic.
    elif non_strobogrammatic_numbers(n):
        return False
    
    # The number is seen different from upside and downside, hence is not strobogrammatic.
    elif not upside_downside_equal(n):
        return False
    
    # Otherwise is strobogrammatic.
    else:
        return True

def main() -> None:
    # Reads a sequence of natural numbers.
    n = scan(int)
    i = 0

    while n is not None:
        if is_strobogrammatic(n):
            print(n, 'is strobogrammatic', sep = ' ', end = '\n')
            if number_lenght(n) % 2 == 1:
                i += 1
        else:
            print(n, 'is not strobogrammatic', sep = ' ', end = '\n')
        n = scan(int)

    print(end = '\n')
    print('odd strobogrammatic: ', i, sep = '', end = '\n')

if __name__ == '__main__':
    main()