from yogi import *
from turtle import *
import jutge

# Es llegeixen dos nombres enters (n) i (m):
n = read(int)
m = read(int)

# Programa principal:
i = 0
j = 0
while i < n:
    while j < n:
        for k in range(4):
            forward(m)
            left(90)

        forward(m)
        j = j + 1

    j = 0
    left(180)
    forward(m * n)
    right(90)
    forward(m)
    right(90)
    i = i + 1
done()
