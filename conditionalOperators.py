name = input("Enter Name")
if name=="Oleg":
    print("True")


num = int(input("Введите число"))
if num > 0:
    print("True")
elif num < 0:
    print("Вы ввели число меньше 0")
else:
    print("Вы ввели 0")

name = input("Введите имя")
a = "Yes" if name != "Test" else "No"
print(a)
