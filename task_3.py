# Напишите функцию, которая отображает пустой или
# заполненный квадрат из некоторого символа. Функция
# принимает в качестве параметров: длину стороны квадрата,
# символ и переменную логического типа:
# если она равна True, квадрат заполненный;
# если False, квадрат пустой.


def square(sym, n, fill=True):
    line = n * sym
    if fill:
        for i in range(n):
            print(line)
    else:
        print(line)
        for i in range(n - 2):
            print(sym + " " * (n - 2) + sym)
        print(line)


square("*", 8, True)
