from yogi import read
import turtle as t
import jutge

def print_fractal(n: int, d: float, x: float, y: float) -> None:
    """Prints the Koch Circles fractal."""

    if n == 1:
        t.circle(d)
    else:
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.circle(d)
        t.penup()
        t.goto(x + d + d / 2, y + d - d / 2)
        t.pendown()
        print_fractal(n - 1, d / 2, x + d + d / 2, y + d - d / 2)
        t.penup()
        t.goto(x - d - d / 2, y + d - d / 2)
        t.pendown()
        print_fractal(n - 1, d / 2, x - d - d / 2, y + d - d / 2)
        t.penup()
        t.goto(x, y + 2 * d)
        t.pendown()
        print_fractal(n - 1, d / 2, x, y + 2 * d)
        t.penup()
        t.goto(x, y - d)
        t.pendown()
        print_fractal(n - 1, d / 2, x, y - d)

def main() -> None:
    # Reads the number of levels of the fractal and,
    # the size.
    n = read(int)
    d = read(float)
    print_fractal(n, d, 0, 0)
    t.speed(0)
    t.done()

if __name__ == '__main__':
    main()