from yogi import read
from turtle import *

# Dibuixa un cercle.
def cercle(r):
    circle(r)

# Dibuixa un quadrat.
def quadrat(c):
    i = 1
    while i <= 4:
        forward(c)
        left(90)
        i = i + 1

# Dibuixa un rectangle.
def rectangle(a, b):
    i = 1
    while i <= 2:
        forward(a)
        left(90)
        forward(b)
        left(90)
        i = i + 1

# Lectura de les dades d'entrada en funció de la forma a dibuixar
# i execució del dibuix.
forma = read(str)

if forma == "cercle":
    r = read(int)
    cercle(r)

elif forma == "quadrat":
    c = read(int)
    quadrat(c)

elif forma == "rectangle":
    a = read(int)
    b = read(int)
    rectangle(a, b)

else:
    print("Forma no reconeguda.")
done()