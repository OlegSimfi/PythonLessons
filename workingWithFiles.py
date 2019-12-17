f = open('text.txt', 'w')
print(f.read())

for line in f:
    print(line)

f.write("Hi, it\'s me!")
f.close()
