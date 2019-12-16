l = []
lis = [1, 56, 'x', 34, 2.34, ['S', 't', 'r', 'o', 'k', 'a']]
print(lis)

a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
print(a)

l.append(23)
l.append(34)
b = [7, 88]
print(l)
l.extend(b)
print(l)
l.insert(1, 77)
print(l)
l.remove(34)
print(l)
l.pop(2)
print(l)
print(l.index(88))
print(l.count(88))
l.sort()
print(l)
l.reverse()
print(l)
l.clear()
print(l)
