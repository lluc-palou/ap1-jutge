from yogi import read

# Es llegeix un nombre enter (n):
n = read(int)

# Programa principal.
while n > 1:
    print(n % 2, end = "")
    n = n // 2
print(n)