from yogi import read

# Es llegeixen dos nombres enters (a) i (b):
a = read(int)
b = read(int)

# Programa principal.
x = a
y = b

while x != y:
    if x > y:
        x = x - y
    else:
        y = y - x
print("The gcd of ", a, " and ", b, " is ", x, ".", sep="")