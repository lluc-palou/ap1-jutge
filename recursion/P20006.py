from yogi import read

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
        return prefixed_expression() - prefixed_expression()
    if (x == '*'):
        return prefixed_expression() * prefixed_expression()
    
def main() -> None:
    print(prefixed_expression(), sep = '', end = '\n')
    
if __name__ == '__main__':
    main()