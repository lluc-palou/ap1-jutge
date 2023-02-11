from yogi import read

def scalar_product(u: list[float], v: list[float]) -> float:
    """Returns the computed scalar product of the two given vectors."""

    lenght = len(u)
    scalar_product = 0.0

    for i in range(lenght):
        scalar_product += u[i] * v[i]

    return scalar_product

def read_sequence(n: int) -> list[float]:
    """Returns a list with the sequence of n real numbers given in 
    the input."""

    List = []

    for i in range(n):
        x = read(float)
        List.append(x)
    
    return List

def main() -> None:
    # Reads two vectors with the same size.
    n = read(int)
    u = read_sequence(n)
    m = read(int)
    v = read_sequence(m)
    print(scalar_product(u, v))

if __name__ == '__main__':
    main()