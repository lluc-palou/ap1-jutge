from yogi import read
from turtle import *
import jutge

# Es llegeixen dos nombres enters (n) i (m):
n = read(int)
m = read(int)

# Programa principal.
i = 1
d = m

while i <= n:
    for j in range(2):
        forward(d)
        left(90)
    i = i + 1
    d = m * i
done()