s = input()

d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
m_char = ''
m_count = -1
for key in d:
    if d[key] > m_count:
        m_count = d[key]
        m_char = key

print(m_char, m_count)