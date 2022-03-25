mas = [1, 2, 3, 4, 5]

n = len(mas)

for i in range(n//2):
    mas[i], mas[n-1 - i] = mas[n-1 - i], mas[i]

print(*mas)


def rev(mas, l=0, r=len(mas)-1):
    while l < r:
        mas[l], mas[r] = mas[r], mas[l]
        l += 1
        r -= 1

rev(mas)
print(*mas)

def shift(mas, p):
    p %= len(mas)
    rev(mas, 0, p-1)
    rev(mas, p, len(mas) - 1)
    rev(mas)