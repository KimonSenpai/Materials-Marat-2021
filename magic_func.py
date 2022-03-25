zip, map, filter, all, any, sum

f = lambda x: x**2 + 1

print(f(20))

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
z = [3, 6, 9, 12]

#I
s = 0
for i in range(len(x)):
    s += (x[i]**2 + y[i]**2 + z[i]**2)**0.5
    
print(s)

#II
s = 0
print(list(zip(x, y, z)))
for X, Y, Z in zip(x, y, z):
    s += (X**2 + Y**2 + Z**2)**0.5

print(s)

#III
s = 0
#print(list(zip(x, y, z)))
for l in zip(x, y, z):
    s += (sum(map(lambda x: x**2, l)))**0.5

print(s)

#IV
f = lambda xx: (sum(map(lambda x: x**2, xx)))**0.5
s = sum(map(f, zip(x, y, z)))
print(s)




print(list(filter(lambda x: x%2 == 0, z)))