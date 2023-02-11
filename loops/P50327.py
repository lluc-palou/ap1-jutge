from yogi import read

# Es llegeix un nombre enter (n):
n = read(int)

# Programa principal:
while n > 9:
    if n % 10 == 0:
        print("0", end="")
    else:
        print(n % 10, end="")
    n = n // 10
print(n)
