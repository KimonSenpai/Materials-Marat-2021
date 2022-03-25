lst = []
for i in range(7):
    lst += [int(input())]

l, r = 0, 6
while l < r:
    lst[l], lst[r] = lst[r], lst[l]
    l += 1
    r -= 1

for i in range(7):
    print(lst[i], end=' ')
print()