from yogi import read
import turtle as t

def draw_histogram(Sequence: list[int], bars: int, width: int) -> None:
    """Draws an histogram of the corresponding sequence."""

    width_column = width / bars
    t.speed(0)

    # Calculates the height of the bars.
    Bars = [0 for _ in range(bars)]

    if bars < 10:
        for i in range(len(Sequence)):
            Bars[(Sequence[i] %  bars) - 1] += 1

    else:
        for i in range(len(Sequence)):
            Bars[(Sequence[i] // bars) - 1] += 1

    height = width / max(Bars)

    # Drawing.
    for i in range(bars):
        t.left(90)
        t.forward(Bars[i] * height)
        t.right(90)
        t.forward(width_column)
        #t.write(i * (width // width_column))
        t.right(90)
        t.forward(Bars[i] * height)
        t.left(90)
    
    t.right(180)
    t.forward(width)

def main() -> None:
    # Reads a natural number (b) corresponding to the number of bars.
    b = read(int)

    # Reads a non empty sequence of natural numbers.
    Sequence: list[int] = []
    n = read(int)

    while n > 0:
        Sequence.append(n)
        n = read(int)

    draw_histogram(Sequence, b, 300)
    t.done()

if __name__ == '__main__':
    main()