i = 0
while i <= 10:
    print(i)
    i += 2


for j in 'hello world':
    if j != 'w':
        continue
    print(j * 3, end='')


for y in 'hello world':
    if y == 'w':
        break
    print(y * 3, end='')


for t in 'hello world':
    if t == 'a':
        break
else:
    print("Буквы а нет")


