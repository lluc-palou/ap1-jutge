from yogi import read

# Es llegeix el nombre de segons (n).
n = 76234

h = n // 3600
m = (n % 3600) // 60
s = n % 60

print(h, m, s)