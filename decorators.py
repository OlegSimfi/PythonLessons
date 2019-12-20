def decorator(func):
    def wrapper():
        print("Code before")
        func()
        print("Code after")

    return wrapper


@decorator
def show():
    print("Im function")


show()
