from yogi import read

def parenthesed_expression() -> int:
    """Returns the result of doing the completely parenthesed
    expressions computations."""

    x = read(str)

    # Base case, situation where x is an operand.
    if (x >= '0') and (x <= '9'):
        return int(x)
    
    # Recursive case, situation whre x is an expression, in fact, 
    # two operands and an operator.
    operand_1 = parenthesed_expression()
    operator = read(str)
    operand_2 = parenthesed_expression()

    # Ugly expressions.
    x = read(str)

    # Computations
    if (operator == '+'):
        return operand_1 + operand_2
    if (operator == '-'):
        return operand_1 - operand_2
    if (operator == '*'):
        return operand_1 * operand_2
    

def main() -> None:
    print(parenthesed_expression(), sep = '', end = '\n')

if __name__ == '__main__':
    main()