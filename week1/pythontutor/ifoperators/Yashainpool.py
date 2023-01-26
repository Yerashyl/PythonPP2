n = int(input())
m = int(input())
x = int(input())
y = int(input())

if n > m:
    n, m = m, n
if x >= n / 2:
    x = n - x
if y >= m / 2:
    y = m - y
print(min(x, y))
