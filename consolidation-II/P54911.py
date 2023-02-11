from yogi import read

def count_pairs() -> int:
    """Returns the number of pairs of elements of the sequence 
    that fullfill the property: x_i-1 + x_i > x_i + x_i+1,"""

    i = 0
    a = read(int)
    if a >= 0:
        b = read(int)
        last_pair = a + b
        while b >= 0:
            current_pair = a + b
            if last_pair > current_pair:
                i += 1
            last_pair = current_pair
            a = b
            b = read(int)
        return i
        
    else:
        return 0
        
def main() -> None:
    
    # Reads several cases.
    s = read(int)
    for i in range(s):
        print(count_pairs(), sep = '', end = '\n')

if __name__ == '__main__':
    main()