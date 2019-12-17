def func(x, a):
    res = x + a
    return res


print(func(27, 77))


def func(*args):
    return args


print(func(1, 2, 3))


def func(x):
    def add(a):
        return x + a

    return add


test = func(100)
print(test(200))
print(test)


def func(r, w, y=2):
    res = r + w
    res *= y
    return res


print(func(2, 4))


def func(*args):
    return args


print(func(2, 4, 3))

add = lambda x, y: x + y
print(add(2, 5))
