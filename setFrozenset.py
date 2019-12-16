a = set("Hello")
a.add(1)
print(type(a))
print(a)

b = frozenset("Qwerty")
print(b)

c = ['r', 's', 'w', 'a', 's', 'w']
print(c)
print(set(c))

d = {32, 45, 43.23, 76}
x = 45
y = {45, 76}
z = {67, 12, 90}
print(len(d))
print(x in d)
print(d.isdisjoint(z))

d.update(z)
print(d)

d.intersection_update(y)
print(d)

d.difference(z)
print(d)

d.symmetric_difference_update(y)
print(d)

d.add(23)
print(d)

d.remove(32)
print(d)

d.discard(32)
print(d)

d.pop()
print(d)

d.clear()
print(d)







