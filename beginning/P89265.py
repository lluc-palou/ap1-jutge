from yogi import read

def main() -> None:
    # Reads the bounds of the two intervals.
    a1 = read(int)
    b1 = read(int)
    a2 = read(int)
    b2 = read(int)

    # Equal intervals.
    if a1 == a2 and b1 == b2:
        print('=', ' , ', '[', a1, ',', b1, ']',  sep = '', end = '\n')
    # [a1, b1] inside [a2, b2]
    elif a2 <= a1 and b1 <= b2:
        print(1, ' , ', '[', a1, ',', b1, ']', sep = '', end = '\n')
    # [a2, b2] inside [a1, b1]
    elif a1 <= a2 and b2 <= b1:
        print(2, ' , ', '[', a2, ',', b2, ']', sep = '', end = '\n')

    else:
        print('?', ' , ', sep = '', end = '')
        # Empty intersection
        if b1 < a2:
            print('[]', sep = '', end = '\n')
        # Empty intersection
        elif b2 < a1:
            print('[]', sep = '', end = '\n')
        # Partial intersection.
        elif a1 <= a2 and b1 <= b2 and a2 <= b1:
            print('[', a2, ',', b1, ']', sep = '', end = '\n')
        # Partial intersection.
        elif a2 <= a1 and b2 <= b1 and a1 <= b2:
            print('[', a1, ',', b2, ']', sep = '', end = '\n')
    
if __name__ == '__main__':
    main()