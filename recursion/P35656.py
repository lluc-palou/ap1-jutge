from yogi import read

def max_2(a: int, b: int) -> int:
    """Computes the maximum of two natural numbers."""

    if a > b:
        return a
    else:
        return b

def max_3(a: int, b: int, c: int) -> int:
    """Computes the maximum of three natural numbers."""

    return(max_2(a, max_2(b, c)))

def prefixed_expression() -> int:
    """Reads the sequence of characters, in fact, the expression and,
    computes the solution."""
    
    x = read(str)

    # Situation where x is a character, operand.
    if (x >= '0' and x <= '9'): 
        return int(x)

    # Situation where x is an operator.
    if (x == '+'):
        return prefixed_expression() + prefixed_expression()
    if (x == '-'):
        return - prefixed_expression()
    if (x == 'm'):
        return max_3(prefixed_expression(), prefixed_expression(), prefixed_expression())
    
def main() -> None:
    print(prefixed_expression(), sep = '', end = '\n')
    
if __name__ == '__main__':
    main()